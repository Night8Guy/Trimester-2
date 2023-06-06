#!/usr/bin/python3
"""
Unittesting for square class
"""
import unittest
from models.square import Square
from io import StringIO
import sys
from unittest.mock import patch, MagicMock
import json


class TestSquare(unittest.TestCase):
    """
    class for testing square class
    """
    def test_valid_attributes_1(self):
        """test valid attribute values x1"""
        square = Square(99)
        self.assertEqual(square.size, 99)

    def test_valid_attributes_2(self):
        """test valid attribute values x2"""
        square = Square(50, 1)
        self.assertEqual(square.size, 50)
        self.assertEqual(square.x, 1)

    def test_valid_attributes_3(self):
        """test valid attribute values x3"""
        square = Square(25, 2, 3)
        self.assertEqual(square.size, 25)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_valid_attributes_4(self):
        """test valid attribute values x4"""
        square = Square(25, 2, 3, 99)
        self.assertEqual(square.size, 25)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 99)

    def test_invalid_size(self):
        """test invalid size values"""
        with self.assertRaises(TypeError):
            Square("string")

    def test_invalid_x(self):
        """test invalid x values"""
        with self.assertRaises(TypeError):
            Square(2, "string")

    def test_invalid_y(self):
        """test invalid y values"""
        with self.assertRaises(TypeError):
            Square(2, 1, "string")

    def test_negative_size(self):
        """test invalid negative size"""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_negative_x(self):
        """test invalid negative x"""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_negative_y(self):
        """test invalid negative y"""
        with self.assertRaises(ValueError):
            Square(1, 2, -4)

    def test_zero_size(self):
        """test zero size"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s1 = Square(5, 2, 3, 99)
        self.assertEqual(str(s1), "[Square] (99) 2/3 - 5")

    def test_to_dict(self):
        s1 = Square(2, 1, 1, 99)

        self.assertEqual(s1.to_dictionary(), {'id': 99, 'size': 2, 'x': 1, 'y': 1})

    def test_update(self):
        s1 = Square(5, 2, 2, 1)
        s1.update(10, 4, 4, 3)
        
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 3)

    def test_create(self):
        s1 = Square.create(**{'id': 89})

        self.assertEqual(s1.id, 89)

    def test_save_to_file_with_none(self):
        # Patch the open function to capture the file output
        with patch('builtins.open', create=True) as mock_open:
            # Call the save_to_file method with None
            Square.save_to_file(None)

            # Assert that open was called with the correct filename
            mock_open.assert_called_once_with('Square.json', 'w')

            # Retrieve the write call arguments
            write_args = mock_open.return_value.__enter__.return_value.write.call_args[0]

            # Convert the JSON string to a dictionary
            saved_data = json.loads(write_args[0])

            # Assert that the saved data is an empty list
            self.assertEqual(saved_data, [])

    def test_save_to_file_with_empty_brackets(self):
        # Patch the open function to capture the file output
        with patch('builtins.open', create=True) as mock_open:
            # Call the save_to_file method with None
            Square.save_to_file([])

            # Assert that open was called with the correct filename
            mock_open.assert_called_once_with('Square.json', 'w')

            # Retrieve the write call arguments
            write_args = mock_open.return_value.__enter__.return_value.write.call_args[0]

            # Convert the JSON string to a dictionary
            saved_data = json.loads(write_args[0])

            # Assert that the saved data is an empty list
            self.assertEqual(saved_data, [])

    def test_save_to_file_with_single_square(self):
        # Create a square instance
        s1 = Square(5)

        # Patch the open function to capture the file output
        with patch('builtins.open', create=True) as mock_open:
            # Call the save_to_file method with a list containing the square
            Square.save_to_file([s1])

            # Assert that open was called with the correct filename
            mock_open.assert_called_once_with('Square.json', 'w')

            # Retrieve the write call arguments
            write_args = mock_open.return_value.__enter__.return_value.write.call_args[0]

            # Convert the JSON string to a dictionary
            saved_data = json.loads(write_args[0])

            # Assert that the saved data is a list with a single square dictionary
            self.assertEqual(len(saved_data), 1)
            self.assertEqual(saved_data[0]['id'], s1.id)
            self.assertEqual(saved_data[0]['size'], s1.size)
            self.assertEqual(saved_data[0]['x'], s1.x)
            self.assertEqual(saved_data[0]['y'], s1.y)

    @patch('builtins.open', new_callable=MagicMock)
    def test_load_from_file_file_not_found(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        mock_open.return_value.__enter__.return_value.read.return_value = ""

        # Call the load_from_file method
        result = Square.load_from_file()

        # Assert that open was called with the correct filename
        mock_open.assert_called_once_with('Square.json', 'r', encoding='utf-8')

        # Assert that the result is an empty list
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
