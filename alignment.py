def needleman_wunsch(seq1, seq2):
    seq1 = seq1.upper()
    seq2 = seq2.upper()

    match = 1
    mismatch = -1
    gap = -2

    n = len(seq1)
    m = len(seq2)

    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # init
    for i in range(n+1):
        matrix[i][0] = i * gap
    for j in range(m+1):
        matrix[0][j] = j * gap

    # fill
    for i in range(1, n+1):
        for j in range(1, m+1):
            if seq1[i-1] == seq2[j-1]:
                diag = matrix[i-1][j-1] + match
            else:
                diag = matrix[i-1][j-1] + mismatch

            up = matrix[i-1][j] + gap
            left = matrix[i][j-1] + gap

            matrix[i][j] = max(diag, up, left)

    # traceback
    aligned1 = ""
    aligned2 = ""

    i, j = n, m

    while i > 0 and j > 0:
        current = matrix[i][j]
        diag = matrix[i-1][j-1]
        up = matrix[i-1][j]
        left = matrix[i][j-1]

        if seq1[i-1] == seq2[j-1]:
            score_diag = diag + match
        else:
            score_diag = diag + mismatch

        if current == score_diag:
            aligned1 = seq1[i-1] + aligned1
            aligned2 = seq2[j-1] + aligned2
            i -= 1
            j -= 1

        elif current == up + gap:
            aligned1 = seq1[i-1] + aligned1
            aligned2 = "-" + aligned2
            i -= 1

        else:
            aligned1 = "-" + aligned1
            aligned2 = seq2[j-1] + aligned2
            j -= 1

    while i > 0:
        aligned1 = seq1[i-1] + aligned1
        aligned2 = "-" + aligned2
        i -= 1

    while j > 0:
        aligned1 = "-" + aligned1
        aligned2 = seq2[j-1] + aligned2
        j -= 1

   
    match_line = ""
    matches = 0

    for a, b in zip(aligned1, aligned2):
        if a == b:
            match_line += "|"
            matches += 1
        else:
            match_line += " "

    identity = (matches / len(aligned1)) * 100

    print("\n--- Alignment Result ---")
    print(aligned1)
    print(match_line)
    print(aligned2)

    print(f"\nScore: {matrix[n][m]}")
    print(f"Identity: {round(identity, 2)}%")



def get_alignment_score(seq1, seq2):
    seq1 = seq1.upper()
    seq2 = seq2.upper()

    match = 1
    mismatch = -1
    gap = -2

    n = len(seq1)
    m = len(seq2)

    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        matrix[i][0] = i * gap
    for j in range(m+1):
        matrix[0][j] = j * gap

    for i in range(1, n+1):
        for j in range(1, m+1):
            if seq1[i-1] == seq2[j-1]:
                diag = matrix[i-1][j-1] + match
            else:
                diag = matrix[i-1][j-1] + mismatch

            up = matrix[i-1][j] + gap
            left = matrix[i][j-1] + gap

            matrix[i][j] = max(diag, up, left)

    return matrix[n][m]

def fasta_similarity_matrix(sequences):
    n = len(sequences)

    print("\n--- Similarity Matrix (Alignment Score) ---")

    # header
    print("     ", end="")
    for i in range(n):
        print(f"S{i+1:>5}", end="")
    print()

    for i in range(n):
        print(f"S{i+1:>5}", end="")

        for j in range(n):
            if i == j:
                score = "-"
            else:
                score = get_alignment_score(sequences[i], sequences[j])

            print(f"{str(score):>5}", end="")

        print()
    print("\n--- Pairwise Alignment Scores ---")

    for i in range(len(sequences)):
        for j in range(i+1, len(sequences)):
            seq1 = sequences[i]
            seq2 = sequences[j]

            score = get_alignment_score(seq1, seq2)

            print(f"Seq{i+1} vs Seq{j+1} → Score: {score}")




def save_similarity_csv(sequences, filename="similarity_matrix.csv"):
    import csv

    n = len(sequences)

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)

        # header
        header = [""] + [f"S{i+1}" for i in range(n)]
        writer.writerow(header)

        for i in range(n):
            row = [f"S{i+1}"]
            for j in range(n):
                if i == j:
                    row.append("-")
                else:
                    score = get_alignment_score(sequences[i], sequences[j])
                    row.append(score)
            writer.writerow(row)