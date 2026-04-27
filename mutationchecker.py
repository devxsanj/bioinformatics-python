def compare_dna(seq1, seq2):
    seq1 = seq1.upper()
    seq2 = seq2.upper()

    if len(seq1) != len(seq2):
        print("Sequences must be of same length")
        return

    print("\nMutations found:")

    mutation_found = False

    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            print(f"Position {i+1}: {seq1[i]} -> {seq2[i]}")
            mutation_found = True

    if not mutation_found:
        print("No mutations found. Sequences are identical.")


# Input
dna1 = input("Enter first DNA sequence: ")
dna2 = input("Enter second DNA sequence: ")

compare_dna(dna1, dna2)