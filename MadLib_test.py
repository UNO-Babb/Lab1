import unittest
from unittest.mock import patch
from io import StringIO
import string
import MadLib

class TestMadLib(unittest.TestCase):
    input_items = [
        "John",        # name
        "25",          # age
        "Blue",        # favorite color
        "Reading",     # hobby
        "Omaha",       # city
        "Astronaut",   # dream job
        "Pizza",       # favorite food
        "Dogs",        # favorite pet
        "Swimming",    #verb
        "Wagon",       #noun
        "Golf"         #sport
    ]
    @patch('builtins.input', side_effect= input_items)
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_input):
        # Call the main function
        MadLib.main()

        # Check the output

        output = mock_stdout.getvalue().strip()
        output = output.translate(str.maketrans('', '', string.punctuation))
        output_list = output.split()
        for i in range(6):
            self.assertIn(TestMadLib.input_items[i], output_list)

if __name__ == '__main__':
    unittest.main()
