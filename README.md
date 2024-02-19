
# ASSIGNMENT 3 -Sree Poojitha P

# secondary_structure_splitter.py

## Description
`secondary_structure_splitter.py` is a Python script designed to split a FASTA file into sequences based on their headers. 
It separates protein sequences from secondary structure sequences, counting the occurrences of each in the input file. I took help from code review 1 & 2 
to write this program.

## Usage

- Run the script using the command line and provide the input FASTA file:
    ```bash
  python3 secondary_structure_splitter.py --infile ss.txt
  python3 secondary_structure_splitter.py -h
  python3 secondary_structure_splitter.py
  python3 secondary_structure_splitter.py --infile ss_designed2Fail.txt
    ```

### Input format:
Ensure the input file is a properly formatted FASTA file with header lines and sequence lines.

### Output
we run the command on terminal to get the output



## nt_fasta_stats.py

### Description
This Python script, `nt_fasta_stats.py`, is designed to generate nucleotide statistics from a FASTA file and write the statistics to an output file.
It calculates the count of nucleotides (A, T, G, C, N), sequence length, and GC percentage for each sequence in the provided FASTA file. 
I used stackover flow and greekforgeeks to write this program.

### Usage
- Run the script using the command line with the required arguments:
    ```bash
    python3 nt_fasta_stats.py --infile influenza.fasta --outfile influenza.stats.txt
    python3 nt_fasta_stats.py -h
    python3 nt_fasta_stats.py
    python3 nt_fasta_stats.py --infile influenza.fasta
    ```

### Input Format
Ensure the input file is in valid FASTA format with sequence headers starting with `>` and the corresponding nucleotide sequence on the following lines.
### Output
we run the command on terminal to get the output


# test_nt_fasta_stats.py

## Description
`test_nt_fasta_stats.py` is a set of unit tests designed to validate the functionality of the functions in the `nt_fasta_stats.py` file. These tests cover critical functions responsible for processing and analyzing FASTA files to compute nucleotide statistics.
I used stackover flow and greekforgeeks to write this program.

## Tests
The unit tests included in this file ensure the following functionalities:

- **get_filehandle:** Validates the function's ability to handle file openings.
- **get_fasta_lists:** Checks the accurate extraction of headers and sequences from a FASTA file.
- **_verify_lists:** Verifies if the lists of headers and sequences are of the same length.
- **_get_num_nucleotides:** Tests the counting of nucleotides in a given sequence.
- **_get_ncbi_accession:** Validates the extraction of the accession number from the header string.
- **output_seq_statistics:** Ensures the accurate calculation and output of sequence statistics.

## How to Run the Tests
- Run the tests by executing the script:
  ```bash
  pytest test_nt_fasta_stats.py
  

  
# test_secondary_structure_splitter.py

## Description
`test_secondary_structure_splitter.py` contains a set of test cases developed to validate the functionalities in the `secondary_structure_splitter.py` script. These tests cover the handling of file operations, argument parsing, and various functions critical to processing and analyzing FASTA files for protein sequences and secondary structures.
I used stackover flow and greekforgeeks to write this program.

## Tests
The unit tests within this script ensure the following functionalities:
- **get_cli_args:** Tests the argument parsing using the `argparse` module.
- **get_filehandle:** Validates file opening functionality and error handling.
- **get_fasta_lists:** Checks the accurate extraction of headers and sequences from a file-like object.
- **_verify_lists:** Verifies if lists of headers and sequences are of the same length.

## How to Run the Tests
- Run the tests using the `pytest` command:
  ```bash
  pytest test_secondary_structure_splitter.py








