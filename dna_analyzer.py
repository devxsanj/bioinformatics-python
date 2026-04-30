def analyze_dna(sequence):
    sequence = sequence.upper()

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


    print("Length:", length)
    print(f"A: {a} ({round((a/length)*100, 2)}%)")
    print(f"T: {t} ({round((t/length)*100, 2)}%)")
    print(f"G: {g} ({round((g/length)*100, 2)}%)")
    print(f"C: {c} ({round((c/length)*100, 2)}%)")
    print("GC Content:", round(gc_content, 2), "%")


dna = input("Enter DNA sequence: ")

analyze_dna(dna)