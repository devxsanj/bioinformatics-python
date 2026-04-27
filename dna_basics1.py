def analyze_dna(sequence):
    sequence = sequence.upper()

    length = len(sequence)

    a = sequence.count('A')
    t = sequence.count('T')
    g = sequence.count('G')
    c = sequence.count('C')


    gc_content = ((g + c) / length) * 100


    print("Length:", length)
    print("A:", a, "T:", t, "G:", g, "C:", c)
    print("GC Content:", round(gc_content, 2), "%")



dna = input("Enter DNA sequence: ")

analyze_dna(dna)