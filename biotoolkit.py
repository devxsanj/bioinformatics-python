def analyze_dna(sequence):
    sequence = sequence.upper()

    # Validation
    valid = {'A', 'T', 'G', 'C'}
    if not set(sequence).issubset(valid):
        print("Invalid DNA sequence. Use only A, T, G, C.")
        return

    length = len(sequence)

    a = sequence.count('A')
    t = sequence.count('T')
    g = sequence.count('G')
    c = sequence.count('C')

    gc_content = ((g + c) / length) * 100

    print("\nDNA Analysis:")
    print("Length:", length)
    print(f"A: {a} ({round((a/length)*100, 2)}%)")
    print(f"T: {t} ({round((t/length)*100, 2)}%)")
    print(f"G: {g} ({round((g/length)*100, 2)}%)")
    print(f"C: {c} ({round((c/length)*100, 2)}%)")
    print("GC Content:", round(gc_content, 2), "%")


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


# 🔹 MAIN MENU LOOP
while True:
    print("\n--- Bioinformatics Toolkit ---")
    print("1. Analyze DNA")
    print("2. Compare DNA")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        dna = input("Enter DNA sequence: ")
        analyze_dna(dna)

    elif choice == "2":
        dna1 = input("Enter first DNA sequence: ")
        dna2 = input("Enter second DNA sequence: ")
        compare_dna(dna1, dna2)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")