"""
Sree Poojitha Paruchuri
secondary_structure_splitter.py
"""

import sys
import argparse


def get_cli_args():
    """
    Command line options using argparse
    """

    parser = argparse.ArgumentParser(description='Provide a FASTA file to perform '
                                                 'splitting on sequence and secondary structure')

    parser.add_argument('-i', '--infile', dest='infile', type=str,
                        help='Path to file to open', required=True)
    cli_args = parser.parse_args()
    return cli_args


def get_filehandle(file_name, mode):
    """Function to get file handle with specified mode"""
    # Try to open the file, catching OS Errors and Value Errors
    try:
        file = open(file_name, mode, encoding="UTF-8")
        return file
    except OSError:
        raise OSError("Specified file does not exist.")
    except ValueError:
        raise ValueError("Incorrect mode specified.")


def get_fasta_lists(file_handle):
    """Function to get header list and sequence list from FASTA file"""

    list_seqs = []
    list_headers = []

    current_sequence = ""
    # Iterate over the file and separate headers and sequences
    for line in file_handle:
        line = line.replace("\n", "")
        # Check if the line is a header line or a sequence line.
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
    Function to verify if header and sequence lists are of the same length
    """

    # Check if the length of the header list and sequence list are the same.
    if len(list_headers) != len(list_seqs):
        error_message = """
        Header and Sequence lists size are different in size
        Did you provide a FASTA formatted file?
        """
        sys.exit(error_message)
    else:
        return True


def main():
    """Main driver function"""

    # Get CLI arguments.
    cli_args = get_cli_args()
    infile = cli_args.infile

    input_file = get_filehandle(infile, "r")
    sequence_file = get_filehandle("pdb_protein.fasta", "w")
    secondary_file = get_filehandle("pdb_ss.fasta", "w")

    list_headers, list_seqs = get_fasta_lists(input_file)

    proteins = 0
    secondary_structures = 0

    # Write proteins and secondary sequences to respective files.
    for i in range(len(list_headers)):
        if "sequence" in list_headers[i]:
            proteins += 1
            sequence_file.write(list_headers[i] + "\n")
            sequence_file.write(list_seqs[i] + "\n")
        else:
            secondary_structures += 1
            secondary_file.write(list_headers[i] + "\n")
            secondary_file.write(list_seqs[i] + "\n")

    # Print output to stdout
    print(f"Found {proteins} protein sequences.")
    print(f"Found {secondary_structures} ss sequences.")

    input_file.close()
    sequence_file.close()
    secondary_file.close()


if __name__ == "__main__":
    main()
