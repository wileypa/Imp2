import random

# def neucleotides
nucleotides = ['A', 'G', 'T', 'C']


def gen_rand_sequence(length):
    return ''.join(random.choice(nucleotides) for _ in range(length))


def gen_rand_pairs(length, num_pairs=10):
    pairs = []
    for _ in range(num_pairs):
        s1 = gen_rand_sequence(length)
        s2 = gen_rand_sequence(length)
        pairs.append(f"{s1},{s2}")
    return pairs


def save_sequences():
    length = int(input("Enter sequence length: "))
    num_pairs = 10
    filename = f"rand_input_{length}.txt"
    with open(filename, 'w') as f:
        pairs = gen_rand_pairs(length, num_pairs)
        for pair in pairs:
            f.write(pair + "\n")

    print(f"Random sequences for length {length} saved to {filename}")


save_sequences()
