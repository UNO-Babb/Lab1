import unittest
from unittest.mock import patch
from io import StringIO
import string
from datetime import datetime
import FirstProgram

class TestFirstProgram(unittest.TestCase):

    @patch('builtins.input', side_effect=["John", "25"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_input):
        # Call the main function
        FirstProgram.main()

        # Check the output
        output = mock_stdout.getvalue().strip()
        output = output.translate(str.maketrans('', '', string.punctuation))
        output_list = output.split()
        year = str(datetime.now().year - 25)
        expected_elements = ["John", year]
        for element in expected_elements:
            self.assertIn(element, output_list)

if __name__ == '__main__':
    unittest.main()
