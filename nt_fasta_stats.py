"""
Sree Poojitha Paruchuri
nt_fasta_stats.py
"""


import sys
import argparse


def get_cli_args():
    """
    Command line options using argparse
    """

    parser = argparse.ArgumentParser(
        description='Provide a FASTA file to generate nucleotide statistics')

    parser.add_argument('-i', '--infile', dest='infile',
                        type=str, help='Path to file to open', required=True)

    parser.add_argument('-o', '--outfile', dest='outfile', type=str,
                        help='Path to file to write', required=True)

    cli_args = parser.parse_args()
    return cli_args


def get_filehandle(file_name, mode):
    """Function to get filehandle with specified mode"""
    # Try to open file, catching OS Errors and Value Errors
    try:
        file = open(file_name, mode)
        return file
    except OSError:
        raise OSError("Specified file does not exist.")
    except ValueError:
        raise ValueError("Incorrect mode specified.")


def get_fasta_lists(file_handle):
    """Function to get header list and sequence list from fast file"""
    list_seqs = []
    list_headers = []

    current_sequence = ""
    # Iterate over file and separate headers and sequence
    for line in file_handle:
        line = line.replace("\n", "")
        # Check if line is header line or sequence line.
        if ">" in line:
            list_headers.append(line)
            if current_sequence != "":
                list_seqs.append(current_sequence)
                current_sequence = ""
        else:
            current_sequence += line
    if current_sequence != "":
        list_seqs.append(current_sequence)

    _verify_lists(list_headers, list_seqs)

    return list_headers, list_seqs


def _verify_lists(list_headers, list_seqs):
    """
    Function to verify if header and sequence lists are
    of same length
    """

    # Check if length of header list and sequence list
    # are the same.
    if len(list_headers) != len(list_seqs):
        error_message = """
Header and Sequence lists size are different in size
Did you provide a FASTA formatted file? """

        sys.exit(error_message)
    else:
        return True


def _get_num_nucleotides(nucleotide, sequence):
    """Function to get count of nucleotide in sequence"""

    # Check if nucleotide is valid and return count, exit if not valid.
    if nucleotide not in ['A', 'T', 'G', 'C', 'N']:
        sys.exit("Did not code this condition")

    return sequence.count(nucleotide)


def _get_ncbi_accession(header_string):
    """Function to get accession number from header string"""

    # Separate accession number from header string.
    header_string_list = header_string.split(" ")
    accession_number = header_string_list[0][1:]
    return accession_number


def output_seq_statistics(list_headers, list_seqs, output_file):
    """Function to write sequence statistics to output file"""
    head = "Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%\n"
    output_file.write(head)

    for i in range(len(list_headers)):
        # Calculate statistics.
        accession_number = _get_ncbi_accession(list_headers[i])
        frequency_a = _get_num_nucleotides("A", list_seqs[i])
        frequency_g = _get_num_nucleotides("G", list_seqs[i])
        frequency_c = _get_num_nucleotides("C", list_seqs[i])
        frequency_t = _get_num_nucleotides("T", list_seqs[i])
        frequency_n = _get_num_nucleotides("N", list_seqs[i])
        length = len(list_seqs[i])
        # Calculate gc percentage.
        gc_percentage = ((frequency_g + frequency_c) / length) * 100
        output_file.write(f"{i + 1}\t{accession_number}")
        output_file.write(f"\t{frequency_a}\t{frequency_g}")
        output_file.write(f"\t{frequency_c}\t{frequency_t}")
        output_file.write(f"\t{frequency_n}\t{length}")
        output_file.write(f"\t{gc_percentage:.1f}\n")


def main():
    """Main driver function"""

    # Get CLI arguments.
    cli_args = get_cli_args()

    infile = cli_args.infile
    outfile = cli_args.outfile

    input_file = get_filehandle(infile, "r")
    output_file = get_filehandle(outfile, "w")

    # Get lists and write statistics to output file.
    list_headers, list_seqs = get_fasta_lists(input_file)
    output_seq_statistics(list_headers, list_seqs, output_file)

    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()
