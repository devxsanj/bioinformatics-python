def read_fasta_multiple(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    sequences = []
    current_seq = ""

    for line in lines:
        if line.startswith(">"):
            if current_seq:
                sequences.append(current_seq)
                current_seq = ""
        else:
            current_seq += line.strip()

    if current_seq:
        sequences.append(current_seq)

    return sequences