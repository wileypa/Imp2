from check_cost import read_cost_matrix

#make a matrix from the input and label as D
#   T A A C T
# A 
# C
# C
# T
# A

# make a pointer matrix to store where each connection would be as ptr
#   T A A C T (not within)
# A R L R R L
# C L L R R R
# C R O R R L
# T O L O R L
# A R L R R L
#(not within)

#will get the starting point based on last column to find smallest
#ptr will tell you which next position is most adventageous and work backwards

#Read in the sequences from imp2input.txt file
def read_sequences(filename):
    with open(filename, 'r') as f:
        line = f.readline().strip() 
    sequence1, sequence2 = line.split(',')
    print("seq1: ", sequence1)
    print("seq2 ", sequence2)
    return sequence1, sequence2


def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print("\t".join(map(str, row)))
    print("\n")


def initialize_matrices(seq1, seq2, loss_matrix, x_indexdict, y_indexdict):
    m = len(seq1) 
    n = len(seq2)
    print("----------------")
    print(f"x_indexdict: {x_indexdict}")
    D = [[0] * (n + 1) for x in range(m + 1)] #creates blank matrix initialized to 0
    ptr = [[None] * (n + 1) for x in range(m + 1)] #creates blank matrix initialized to None

    for i in range(1, m+1):
        row = x_indexdict[seq1[i-1]]
        D[i][0] = D[i - 1][0] + loss_matrix[row][-1] 
        ptr[i][0] = 'D'  
    for j in range(1, n+1):
        column = y_indexdict[seq2[j-1]]
        D[0][j] = D[0][j - 1] + loss_matrix[-1][column]
        ptr[0][j] = 'L'
    
    print_matrix(D, "D Matrix")
    print_matrix(ptr, "Pointer Matrix")
    return D, ptr





def diff(a, b):
    if a == b:
        return 0
    return 1 # if a != b







def edit_dist(seq1, seq2, loss_matrix, x_indexdict, y_indexdict): #m is length of x (horizontal), n is length of y (vertical), s = index of horizontal, t is index of vertical
    i = 0
    j = 0
    m = len(seq1)
    n = len(seq2)
    direction = 0

    D, ptr = initialize_matrices(seq1, seq2, loss_matrix, x_indexdict, y_indexdict)

    for i in range(1, m+1):
        for j in range(1, n+1):
            D[i][j] = min(
                        D[i-1][j] + 1,
                        D[i][j-1] + 1,
                        D[i-1][j-1] + diff(seq1[i - 1], seq2[j - 1]))
            if D[i][j] == D[i-1][j] + 1:
                direction = 'U' #up
            elif D[i][j] == D[i][j-1] + 1:
                direction = 'L' #left 
            elif D[i][j] == D[i-1][j-1]:
                direciton = 'D' #diag

            #assign the ptr based on which direction is is
            if direction == 'U': #point to the one to the up
                ptr[i][j] = direction 
            elif direction == 'L': #point to the one to the left
                ptr[i][j] = direction
            elif direction == 'D': #point to the one diagonally
                ptr[i][j] = 'D' 
    
    print_matrix(D, "D Matrix")
    print_matrix(ptr, "Pointer Matrix")
    
    return D, ptr




def backtracing(ptr, seq1, seq2):
    aligned_seq1 = []
    aligned_seq2 = []
    i = len(seq1)
    j = len(seq2)

    #i = 4
    #j = 4

    # while i > 0 or j > 0:
    #     #want to map out the pointer
    #     print("here")



matrix_info = read_cost_matrix("imp2cost.txt")
sequences = read_sequences("imp2input.txt")
D, ptr = edit_dist(sequences[0], sequences[1], matrix_info[0], matrix_info[1], matrix_info[2])
aligned1, aligned2 = backtracing(ptr, sequences[0], sequences[1])