from fasta_reader import read_fasta_multiple
from fasta_report import save_fasta_report
from dna_analyzer import analyze_dna
from mutationchecker import compare_dna
from sequence_comparison import compare_summary, save_comparison_report


while True:
    print("\n--- Bioinformatics Toolkit ---")
    print("1. Analyze DNA")
    print("2. Compare DNA")
    print("3. Analyze FASTA file")
    print("4. Compare with summary")
    print("5. Save comparison report")
    print("6. Save FASTA analysis report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        dna = input("Enter DNA sequence: ")
        analyze_dna(dna)

    elif choice == "2":
        dna1 = input("Enter first DNA sequence: ")
        dna2 = input("Enter second DNA sequence: ")
        compare_dna(dna1, dna2)

    elif choice == "3":
            file = input("Enter FASTA file: ")
            seqs = read_fasta_multiple(file)

            for i, seq in enumerate(seqs, start=1):
                    print(f"\n--- Sequence {i} ---")
                    analyze_dna(seq)

    elif choice == "4":
        dna1 = input("Enter first DNA sequence: ")
        dna2 = input("Enter second DNA sequence: ")
        compare_summary(dna1, dna2)
    
    elif choice == "5":
            dna1 = input("Enter first DNA sequence: ")
            dna2 = input("Enter second DNA sequence: ")
            save_comparison_report(dna1, dna2)
            print("Report saved as comparison_report.txt")
    
    
    elif choice == "6":
            file = input("Enter FASTA file: ")
            seqs = read_fasta_multiple(file)
            save_fasta_report(seqs)
            print("Report saved as fasta_report.txt")

    elif choice == "7":
            print("Exiting program...")
            break

    else:
        print("Invalid choice. Try again.")