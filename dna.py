from Bio.Seq import Seq

def dna_to_rna(dna_sequence):
    dna_seq = Seq(dna_sequence)
    rna_sequence = dna_seq.transcribe()
    return str(rna_sequence)

def rna_to_protein(rna_sequence):
    rna_seq = Seq(rna_sequence)
    protein_sequence = rna_seq.translate()
    return str(protein_sequence)

def is_valid_dna(dna_sequence):
    return all(base in "ATCG" for base in dna_sequence.upper())

def main():
    print("Welcome to the DNA Sequence Analyzer")
    dna_sequence = input("Enter a DNA sequence: ").upper()

    if not is_valid_dna(dna_sequence):
        print("Invalid DNA sequence. Please only use A, T, C, and G.")
        return

    rna_sequence = dna_to_rna(dna_sequence)
    protein_sequence = rna_to_protein(rna_sequence)

    print("\nResults:")
    print(f"DNA Sequence: {dna_sequence}")
    print(f"RNA Sequence: {rna_sequence}")
    print(f"Protein Sequence: {protein_sequence}")

if __name__ == "__main__":
    main()
