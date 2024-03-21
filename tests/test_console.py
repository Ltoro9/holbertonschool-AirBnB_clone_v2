#!/usr/bin/python3
"""Unit tests for the HBNB console"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the HBNB console"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """Test quit command"""
        with patch('sys.stdin', StringIO('quit\n')):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), '(hbnb) ')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test create command"""
        with patch('sys.stdin', StringIO('create BaseModel\n')):
            HBNBCommand().cmdloop()
            self.assertIn("[BaseModel]", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test show command"""
        with patch('sys.stdin',
                   StringIO('create BaseModel\nshow BaseModel\n')):
            HBNBCommand().cmdloop()
            self.assertIn("[BaseModel]", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Test destroy command"""
        with patch('sys.stdin',
                   StringIO('create BaseModel\ndestroy BaseModel\n')):
            HBNBCommand().cmdloop()
            self.assertEqual("(hbnb) ", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Test all command"""
        with patch('builtins.input', side_effect=['all', 'EOF']):
            HBNBCommand().cmdloop()
        print("Actual Output:", repr(mock_stdout.getvalue()))
        self.assertIn('[BaseModel]', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """Test update command"""
        with patch('sys.stdin', StringIO
                   ('create BaseModel\nupdate BaseModel 1 name "test"\n')):
            HBNBCommand().cmdloop()
            self.assertEqual("(hbnb) ", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout, mock_input):
        console = HBNBCommand()
        console.cmdloop()  # Simulate entering the command loop
        expected_output = '(hbnb)\n'  # Adjusted expected output to include newline character
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)  # Redirect stdout
    def test_all(self, mock_stdout):
        console = HBNBCommand()
        console.do_all()  # Assuming do_all() is the method to test
        expected_output = "[BaseModel] ("
        self.assertIn(expected_output, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
