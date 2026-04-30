def save_fasta_report(sequences, filename="fasta_report.txt"):
    with open(filename, "w") as f:
        for i, seq in enumerate(sequences, start=1):
            seq = seq.upper()

            length = len(seq)
            a = seq.count('A')
            t = seq.count('T')
            g = seq.count('G')
            c = seq.count('C')

            gc = round(((g + c) / length) * 100, 2)

            f.write(f"--- Sequence {i} ---\n")
            f.write(f"Length: {length}\n")
            f.write(f"A: {a}\n")
            f.write(f"T: {t}\n")
            f.write(f"G: {g}\n")
            f.write(f"C: {c}\n")
            f.write(f"GC Content: {gc}%\n\n")