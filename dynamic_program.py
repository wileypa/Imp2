import sys
from check_cost import read_cost_matrix
from check_cost import get_cost


#Read in the sequences from the input file
#Information on how to read in a line from a file from
#w3schools: https://www.w3schools.com/python/python_file_open.asp
def read_sequences(filename):
    sequences = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip() 
            if line:
                sequence1, sequence2 = line.split(',')
                sequences.append((sequence1, sequence2)) 
    return sequences


def initialize_matrices(seq1, seq2, loss_matrix, x_indexdict, y_indexdict):
    m = len(seq1) 
    n = len(seq2)

    D = [[0] * (n + 1) for x in range(m + 1)] #creates blank matrix initialized to 0
    ptr = [[None] * (n + 1) for x in range(m + 1)] #creates blank matrix initialized to None

    for i in range(1, m+1):
        row = x_indexdict[seq1[i-1]]
        D[i][0] = D[i - 1][0] + loss_matrix[row][0] 
        ptr[i][0] = 'U'  
    for j in range(1, n+1):
        column = y_indexdict[seq2[j-1]]
        D[0][j] = D[0][j - 1] + loss_matrix[0][column]
        ptr[0][j] = 'L'
    return D, ptr



def diff(a, b, cost_matrix, x_indexdict, y_indexdict):
    if a== '-' or b == '-':
        return cost_matrix[x_indexdict[a]][y_indexdict[b]]
    return cost_matrix[x_indexdict[a]][y_indexdict[b]]



def edit_dist(seq1, seq2, loss_matrix, x_indexdict, y_indexdict): #m is length of x (horizontal), n is length of y (vertical), s = index of horizontal, t is index of vertical
    i = 0
    j = 0
    m = len(seq1)
    n = len(seq2)
    direction = 0

    D, ptr = initialize_matrices(seq1, seq2, loss_matrix, x_indexdict, y_indexdict)

 

    for i in range(1, m+1):
        for j in range(1, n+1):
            substitution = D[i-1][j-1] + diff(seq1[i - 1], seq2[j - 1], loss_matrix, x_indexdict, y_indexdict)
            insertion = D[i][j-1] + loss_matrix[0][y_indexdict[seq2[j-1]]]
            deletion = D[i-1][j] + loss_matrix[x_indexdict[seq1[i-1]]][0]

            D[i][j] = min(insertion, deletion, substitution)
            if D[i][j] == deletion:
                direction = 'U' #up
            elif D[i][j] == insertion:
                direction = 'L' #left 
            elif D[i][j] == substitution:
                direction = 'D' #diag
            ptr[i][j] = direction
    return D, ptr




def backtracing(ptr, seq1, seq2):
    aligned_seq1 = []
    aligned_seq2 = []
    i = len(seq1)
    j = len(seq2)


    while i > 0 or j > 0:
        if ptr[i][j] is None:
            break
        if ptr[i][j] == 'D': #substitution
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif ptr[i][j] == 'U': #deletion
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append('-')
            i -= 1
        elif ptr[i][j] == 'L': #insertion
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j-1])
            j -= 1
    return list(reversed(aligned_seq1)), list(reversed(aligned_seq2))


costMatrix = "imp2cost.txt"
inputFile = "imp2input.txt"


matrix_info = read_cost_matrix(costMatrix)
sequences = read_sequences(inputFile)

for sequence1, sequence2 in sequences:
    D, ptr = edit_dist(sequence1, sequence2, matrix_info[0], matrix_info[1], matrix_info[2])
    aligned1, aligned2 = backtracing(ptr, sequence1, sequence2)
    cost = get_cost(aligned1, aligned2, matrix_info[0], matrix_info[1], matrix_info[2])
    result1 = ''.join(aligned1)
    result2 = ''.join(aligned2)
    with open("imp2output.txt", "a") as file:
        file.write(f"{result1},{result2}:{cost}\n")
