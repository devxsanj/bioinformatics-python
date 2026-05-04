from biological_insights import sequence_insight
def compare_summary(seq1, seq2):
    seq1 = seq1.upper()
    seq2 = seq2.upper()

    if len(seq1) != len(seq2):
        print("Sequences must be same length")
        return

    matches = 0
    mutations = []

    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            matches += 1
        else:
            mutations.append((i+1, seq1[i], seq2[i]))

    similarity = (matches / len(seq1)) * 100

    print("\n--- Comparison Summary ---")
    print(f"Length: {len(seq1)}")
    print(f"Matches: {matches}")
    print(f"Mutations: {len(mutations)}")
    print(f"Similarity: {round(similarity, 2)}%")

    gc_content = ((seq1.count('G') + seq1.count('C')) / len(seq1)) * 100
    print(f"GC Content: {round(gc_content, 2)}%")

    if mutations:
        print("\nMutation Details:")
        for pos, a, b in mutations:
            print(f"Position {pos}: {a} -> {b}")

    mutation_count = len(mutations)
    gc_content = ((seq1.count('G') + seq1.count('C')) / len(seq1)) * 100

    sequence_insight(seq1, gc_content, mutation_count)

def save_comparison_report(seq1, seq2, filename="comparison_report.txt"):
    seq1 = seq1.upper()
    seq2 = seq2.upper()

    if len(seq1) != len(seq2):
        print("Sequences must be same length")
        return

    matches = 0
    mutations = []

    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            matches += 1
        else:
            mutations.append((i+1, seq1[i], seq2[i]))

    similarity = (matches / len(seq1)) * 100

    with open(filename, "w") as f:
        f.write("--- Comparison Summary ---\n")
        f.write(f"Length: {len(seq1)}\n")
        f.write(f"Matches: {matches}\n")
        f.write(f"Mutations: {len(mutations)}\n")
        f.write(f"Similarity: {round(similarity, 2)}%\n\n")

        if mutations:
            f.write("Mutation Details:\n")
            for pos, a, b in mutations:
                f.write(f"Position {pos}: {a} -> {b}\n")
        else:
            f.write("No mutations found.\n")