"""
Sree Poojitha Paruchuri's Assignment
test_nt_fasta_stats.py
"""

import io
import unittest
from unittest.mock import patch
from nt_fasta_stats import (get_filehandle, get_fasta_lists, _verify_lists,
                            _get_num_nucleotides, _get_ncbi_accession, output_seq_statistics)


class TestNtFastaStatsFunctions(unittest.TestCase):
    """Unit tests for functions in the nt_fasta_stats.py file."""

    def test_get_filehandle(self):
        """Test the get_filehandle function."""
        with patch('builtins.open', return_value=io.StringIO('test')):
            file_handle = get_filehandle('test.txt', 'r')
            self.assertIsNotNone(file_handle)

    def test_get_fasta_lists(self):
        """Test the get_fasta_lists function."""
        test_data = ">Header1\nATCG\n>Header2\nCGTA"
        file_handle = io.StringIO(test_data)
        header_list, seq_list = get_fasta_lists(file_handle)
        self.assertEqual(header_list, [">Header1", ">Header2"])
        self.assertEqual(seq_list, ["ATCG", "CGTA"])

    def test_verify_lists(self):
        """Test the _verify_lists function."""
        # Testing the case where lists are of equal length
        header_list = [">Header1", ">Header2"]
        seq_list = ["ATCG", "CGTA"]
        self.assertTrue(_verify_lists(header_list, seq_list))

        # Testing the case where lists have different lengths
        header_list = [">Header1", ">Header2", ">Header3"]
        seq_list = ["ATCG", "CGTA"]
        with self.assertRaises(SystemExit):
            _verify_lists(header_list, seq_list)

    def test_get_num_nucleotides(self):
        """Test the _get_num_nucleotides function."""
        sequence = "ATCGATCG"
        self.assertEqual(_get_num_nucleotides('A', sequence), 2)
        self.assertEqual(_get_num_nucleotides('G', sequence), 2)
        self.assertEqual(_get_num_nucleotides('C', sequence), 2)
        self.assertEqual(_get_num_nucleotides('T', sequence), 2)
        self.assertEqual(_get_num_nucleotides('N', sequence), 0)

    def test_get_ncbi_accession(self):
        """Test the _get_num_nucleotides function."""
        header_string = ">Header1 some random text"
        self.assertEqual(_get_ncbi_accession(header_string), "Header1")

    def test_output_seq_statistics(self):
        """Test the output_seq_statistics function."""
        header_list = [">Header1", ">Header2"]
        seq_list = ["ATCG", "CGTA"]
        output_file = io.StringIO()
        output_seq_statistics(header_list, seq_list, output_file)

        expected_output = (
            "Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%\n"
            "1\tHeader1\t1\t1\t1\t1\t0\t4\t50.0\n"
            "2\tHeader2\t1\t1\t1\t1\t0\t4\t50.0\n"  # Fixed the G count to match the test case
        )

        expected_output_lines = expected_output.strip().split('\n')
        actual_output_lines = output_file.getvalue().strip().split('\n')

        # Verify if all expected lines are present in the actual output
        for line in expected_output_lines:
            self.assertIn(line, actual_output_lines)

        # Verify if all actual lines are present in the expected output
        for line in actual_output_lines:
            self.assertIn(line, expected_output_lines)


if __name__ == '__main__':
    unittest.main()
