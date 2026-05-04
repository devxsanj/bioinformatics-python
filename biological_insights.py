def sequence_insight(seq, gc_content, mutation_count):
    if gc_content > 60:
        stability = "High"
    elif gc_content >= 40:
        stability = "Moderate"
    else:
        stability = "Low"

    if mutation_count == 0:
        risk = "None"
    elif mutation_count <= 2:
        risk = "Low"
    elif mutation_count <= 5:
        risk = "Moderate"
    else:
        risk = "High"

    if mutation_count == 0:
        interpretation = "No variation detected; sequence conserved"
    elif risk in ["Moderate", "High"]:
        interpretation = "Potential functional impact; further analysis suggested"
    else:
        interpretation = "Minor variation; limited impact likely"

    print("\n--- Biological Insight ---")
    print(f"Sequence Stability: {stability}")
    print(f"Mutation Risk: {risk}")
    print(f"Interpretation: {interpretation}")