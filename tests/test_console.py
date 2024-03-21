#!/usr/bin/python3
"""Unit tests for the HBNB console"""

import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestConsole(unittest.TestCase):
    """Test cases for the HBNB console"""

    def test_all_returns_dict_with_objects(self):
        """Test if all() method returns a dictionary containing objects"""
        new_model = BaseModel()        
        objects_dict = storage.all()
        self.assertIsInstance(objects_dict, dict)
        self.assertIn(new_model.__class__.__name__ + '.' + new_model.id, objects_dict)

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_quit(self, mock_stdout):
    #     """Test quit command"""
    #     with patch('sys.stdin', StringIO('quit\n')):
    #         HBNBCommand().cmdloop()
    #         self.assertEqual(mock_stdout.getvalue(), '(hbnb) ')

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_create(self, mock_stdout):
    #     """Test create command"""
    #     with patch('sys.stdin', StringIO('create BaseModel\n')):
    #         HBNBCommand().cmdloop()
    #         self.assertIn("[BaseModel]", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_show(self, mock_stdout):
    #     """Test show command"""
    #     with patch('sys.stdin',
    #                StringIO('create BaseModel\nshow BaseModel\n')):
    #         HBNBCommand().cmdloop()
    #         self.assertIn("[BaseModel]", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_destroy(self, mock_stdout):
    #     """Test destroy command"""
    #     with patch('sys.stdin',
    #                StringIO('create BaseModel\ndestroy BaseModel\n')):
    #         HBNBCommand().cmdloop()
    #         self.assertEqual("(hbnb) ", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_all(self, mock_stdout):
    #     """Test all command"""
    #     with patch('builtins.input', side_effect=['all', 'EOF']):
    #         HBNBCommand().cmdloop()
    #     print("Actual Output:", repr(mock_stdout.getvalue()))
    #     self.assertIn('[BaseModel]', mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_update(self, mock_stdout):
    #     """Test update command"""
    #     with patch('sys.stdin', StringIO
    #                ('create BaseModel\nupdate BaseModel 1 name "test"\n')):
    #         HBNBCommand().cmdloop()
    #         self.assertEqual("(hbnb) ", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
