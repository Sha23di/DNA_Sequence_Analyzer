# DNA Sequence Analyzer

A simple Python tool for analyzing DNA sequences. This program converts DNA sequences to RNA and then to proteins, providing an easy way to work with basic DNA-to-protein transformations.

## Features

- Converts a DNA sequence to RNA.
- Translates RNA to a protein sequence.
- Checks for valid DNA sequences (ensures only 'A', 'T', 'C', and 'G' bases are used).

## Requirements

- **Python 3.7+**
- **Biopython**: This library is used for handling biological sequences. Install it via pip:

  
  pip install biopython
  

## Usage

1. Clone the repository:

 
   git clone https://github.com/sha23di/DNA_Sequence_Analyzer.git
   cd DNA_Sequence_Analyzer


2. Run the script:

   
   python dna.py
   

3. Enter a DNA sequence when prompted. The program will validate the sequence and then display the corresponding RNA and protein sequences.

### Example


Welcome to the DNA Sequence Analyzer
Enter a DNA sequence: ATGCGTAC

Results:
DNA Sequence: ATGCGTAC
RNA Sequence: AUGCGUAC
Protein Sequence: MR


## Functions

- `dna_to_rna(dna_sequence)`: Converts a DNA sequence to an RNA sequence by transcribing it.
- `rna_to_protein(rna_sequence)`: Converts an RNA sequence to a protein sequence by translating it.
- `is_valid_dna(dna_sequence)`: Checks if a sequence contains only valid DNA bases ('A', 'T', 'C', 'G').

## Contributing

Contributions are welcome! Please submit a pull request or create an issue if you encounter any bugs or have suggestions for new features.

## License

This project is licensed under the MIT License.

---

Enjoy analyzing DNA sequences with this tool!


This `README.md` provides an overview of the project, instructions for setting up and using the script, and information about the main functions.
