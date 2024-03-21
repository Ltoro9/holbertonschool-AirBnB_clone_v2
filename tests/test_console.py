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
        with patch('sys.stdin', StringIO('create BaseModel\nshow BaseModel\n')):
            HBNBCommand().cmdloop()
            self.assertIn("[BaseModel]", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Test destroy command"""
        with patch('sys.stdin', StringIO('create BaseModel\ndestroy BaseModel\n')):
            HBNBCommand().cmdloop()
            self.assertEqual("(hbnb) ", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Test all command"""
        with patch('sys.stdin', StringIO('all\n')):
            HBNBCommand().cmdloop()
            self.assertEqual("['[BaseModel] (", mock_stdout.getvalue()[:19])

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """Test update command"""
        with patch('sys.stdin', StringIO('create BaseModel\nupdate BaseModel 1 name "test"\n')):
            HBNBCommand().cmdloop()
            self.assertEqual("(hbnb) ", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """Test EOF command"""
        with patch('sys.stdin', StringIO('EOF\n')):
            HBNBCommand().cmdloop()
            self.assertEqual('', mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
