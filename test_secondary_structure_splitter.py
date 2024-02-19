"""
Sree Poojitha Paruchuri's Assignment3
test_secondary_structure_splitter.py
"""

import sys
import os
import pytest
from secondary_structure_splitter import get_cli_args, get_fasta_lists, _verify_lists


def get_filehandle(file_name, mode):
    """Function to get file handle with the specified mode"""
    try:
        file = open(file_name, mode, encoding="UTF-8")
        return file
    except FileExistsError:
        if mode == 'x':
            raise FileExistsError("File already exists, cannot create a new file in 'x' mode.")
        raise
    except OSError as os_error:
        raise OSError(f"An OS-related error occurred: {os_error}")
    except ValueError:
        raise ValueError("Invalid mode provided")


def test_get_cli_args():
    """Test argument parsing using the argparse module"""
    sys.argv = ['secondary_structure_splitter.py', '-i', 'test.fasta']
    args = get_cli_args()
    assert args.infile == 'test.fasta'


def test_get_filehandle():
    """Test file opening"""
    file_name = 'test.fasta'
    mode = 'r'
    file_handle = get_filehandle(file_name, mode)
    assert file_handle is not None
    file_handle.close()

    # Test handling non-existing file
    file_name = 'non_existing_file.fasta'
    mode = 'r'
    with pytest.raises(OSError):
        get_filehandle(file_name, mode)

    # Test handling an existing file in 'x' mode
    file_name = 'test_existing_file.fasta'
    mode = 'x'
    with open(file_name, 'w'):
        pass
    with pytest.raises(FileExistsError):
        get_filehandle(file_name, mode)
    os.remove(file_name)  # Remove the created file after the test


def test_get_fasta_lists():
    """Test get_fasta_lists function"""
    file_handle = ['>header1\n', 'sequence1\n', '>header2\n', 'sequence2\n']
    list_headers, list_seqs = get_fasta_lists(file_handle)
    assert list_headers == ['>header1', '>header2']
    assert list_seqs == ['sequence1', 'sequence2']

    file_handle = ['>header1\n', 'sequence1\n', '>header2\n']
    with pytest.raises(SystemExit):
        get_fasta_lists(file_handle)


def test_verify_lists():
    """Test _verify_lists function"""
    list_headers = ['>header1', '>header2']
    list_seqs = ['sequence1', 'sequence2']
    result = _verify_lists(list_headers, list_seqs)
    assert result is True

    list_headers = ['>header1', '>header2']
    list_seqs = ['sequence1']
    with pytest.raises(SystemExit):
        _verify_lists(list_headers, list_seqs)
