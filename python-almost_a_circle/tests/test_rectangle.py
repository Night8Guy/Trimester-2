'''test_rectangle module'''
import unittest
import os
import sys
import json
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch, MagicMock

class TestRectangle(unittest.TestCase):
    '''class docstring for TestRectangle'''
    def setUp(self):
        '''redirect stdout to check output from display()'''
        self.output = StringIO()
        sys.stdout = self.output

        self.rectangle = Rectangle(4, 5)

        # reset nb_objects to 0 before each test
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''clean up after test_display() to restore stdout'''
        sys.stdout = sys.__stdout__

        del self.rectangle
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
    def test_valid_attributes(self):
        '''test valid attribute values'''
        rectangle = Rectangle(10, 20, 5, 5)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 5)

    def test_invalid_width(self):
        '''test invalid width values (non-int & value <= 0)'''
        with self.assertRaises(TypeError):
            Rectangle("invalid", 20, 5, 5)

        with self.assertRaises(ValueError):
            Rectangle(0, 20, 5, 5)

        with self.assertRaises(ValueError):
            Rectangle(-10, 20, 5, 5)

    def test_invalid_height(self):
        '''test invalid height values (non-int & value <= 0)'''
        with self.assertRaises(TypeError):
            Rectangle(10, "invalid", 5, 5)

        with self.assertRaises(ValueError):
            Rectangle(0, 20, 5, 5)

        with self.assertRaises(ValueError):
            Rectangle(10, -5, 5, 5)

        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_invalid_x(self):
        '''test invalid x values (non-int & value <= 0)'''

        with self.assertRaises(TypeError):
            Rectangle(10, 20, "invalid", 5)

        with self.assertRaises(ValueError):
            Rectangle(10, 20, -5, 5)

    def test_invalid_y(self):
        '''test invalid y values (non-int & value <= 0)'''

        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, "invalid")

        with self.assertRaises(ValueError):
            Rectangle(10, 20, 5, -5)

    def test_area(self):
        '''test if Rectangle instances calculate area properly '''
        # Test case 1: Width = 4, Height = 5
        rectangle1 = Rectangle(4, 5)
        self.assertEqual(rectangle1.area(), 20)

        # Test case 2: Width = 7, Height = 3
        rectangle1 = Rectangle(7, 3)
        self.assertEqual(rectangle1.area(), 21)

        # Test case 3: Width = 10, Height = 10
        rectangle1 = Rectangle(10, 10)
        self.assertEqual(rectangle1.area(), 100)

    def test_display(self):
        '''test display() method'''
        self.rectangle = Rectangle(4, 5)
        self.rectangle.display()
        self.assertEqual(self.output.getvalue(),
                                    "####\n####\n####\n####\n####\n")

    def test_display_with_x(self):
        # Test display with x
        self.rectangle = Rectangle(2, 2, 2)
        self.rectangle.display()
        self.assertEqual(self.output.getvalue(), "  ##\n  ##\n")

    def test_display_with_y(self):
        # Test display with x and y
        self.rectangle = Rectangle(2, 2, 2, 2)
        self.rectangle.display()
        self.assertEqual(self.output.getvalue(), "\n\n  ##\n  ##\n")    

    def test_str1(self):
        '''compare the output of str(rectangle) with the expected output'''
        # Test case 1
        rectangle1 = Rectangle(4, 5, 2, 3, 1)
        expected_output1 = "[Rectangle] (1) 2/3 - 4/5"
        self.assertEqual(str(rectangle1), expected_output1)

    def test_str2(self):
        '''compare the output of str(rectangle) with the expected output'''
        # Test case 2
        rectangle2 = Rectangle(7, 3, 1, 2, 2)
        expected_output2 = "[Rectangle] (2) 1/2 - 7/3"
        self.assertEqual(str(rectangle2), expected_output2)

    def test_str3(self):
        '''compare the output of str(rectangle) with the expected output'''
        # Test case 3
        rectangle3 = Rectangle(2, 2, 0, 0, 3)
        expected_output3 = "[Rectangle] (3) 0/0 - 2/2"
        self.assertEqual(str(rectangle3), expected_output3)

    def test_to_dictionary(self):
        '''test to_dictionary() method'''
        # Test case 1
        rectangle1 = Rectangle(10, 2, 1, 9)
        expected_output1 = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(rectangle1.to_dictionary(), expected_output1)

        # Test case 2
        rectangle2 = Rectangle(1, 1)
        expected_output2 = {'x': 0, 'y': 0, 'id': 2, 'height': 1, 'width': 1}
        self.assertEqual(rectangle2.to_dictionary(), expected_output2)

        # Test case 3
        rectangle3 = Rectangle(10, 2, 0, 0, 12)
        expected_output3 = {'x': 0, 'y': 0, 'id': 12, 'height': 2, 'width': 10}
        self.assertEqual(rectangle3.to_dictionary(), expected_output3)

    def test_update_positional_args(self):
        """ test update method:
        assigns an argument to each attribute
        """
        # test update id
        self.rectangle.update(10)
        self.assertEqual(self.rectangle.id, 10)
        # test update width
        self.rectangle.update(10, 20)
        self.assertEqual(self.rectangle.width, 20)
        # test update height
        self.rectangle.update(10, 20, 30)
        self.assertEqual(self.rectangle.height, 30)
        # test update x
        self.rectangle.update(10, 20, 30, 40)
        self.assertEqual(self.rectangle.x, 40)
        # test update y
        self.rectangle.update(10, 20, 30, 40, 50)
        self.assertEqual(self.rectangle.y, 50)

    def test_update_kw_args(self):
        """Test updating attributes with keyword arguments"""
        rectangle = Rectangle(1, 1, 1, 1, 1)
        rectangle.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 6)

    def test_update_args_and_kwargs(self):
        """ test update method:
        assigns an argument to each attribute using *args and **kwargs
        """
        rectangle = Rectangle(1, 1, 1, 1, 1)
        rectangle.update(2, 3, 4, 5, 6, id=7, width=8, height=9, x=10, y=11)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 6)

    def test_save_to_file(self):
        '''test save_to_file() method'''
        # Test case 1
        rectangle1 = Rectangle(10, 7, 2, 8)
        rectangle2 = Rectangle(2, 4)
        Rectangle.save_to_file([rectangle1, rectangle2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                [rectangle1.to_dictionary(), rectangle2.to_dictionary()],
                Base.from_json_string(f.read())
            )

    def test_create(self):
        r1 = Rectangle.create(**{'id': 89})

        self.assertEqual(r1.id, 89)

    def test_save_to_file_with_none(self):
        # Patch the open function to capture the file output
        with patch('builtins.open', create=True) as mock_open:
            # Call the save_to_file method with None
            Rectangle.save_to_file(None)

            # Assert that open was called with the correct filename
            mock_open.assert_called_once_with('Rectangle.json', 'w')

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
            Rectangle.save_to_file([])

            # Assert that open was called with the correct filename
            mock_open.assert_called_once_with('Rectangle.json', 'w')

            # Retrieve the write call arguments
            write_args = mock_open.return_value.__enter__.return_value.write.call_args[0]

            # Convert the JSON string to a dictionary
            saved_data = json.loads(write_args[0])

            # Assert that the saved data is an empty list
            self.assertEqual(saved_data, [])

    def test_save_to_file_with_single_rectangle(self):
        # Create a rectangle instance
        r1 = Rectangle(1, 2)

        # Patch the open function to capture the file output
        with patch('builtins.open', create=True) as mock_open:
            # Call the save_to_file method with a list containing the rectangle
            Rectangle.save_to_file([r1])

            # Assert that open was called with the correct filename
            mock_open.assert_called_once_with('Rectangle.json', 'w')

            # Retrieve the write call arguments
            write_args = mock_open.return_value.__enter__.return_value.write.call_args[0]

            # Convert the JSON string to a dictionary
            saved_data = json.loads(write_args[0])

            # Assert that the saved data is a list with a single rectangle dictionary
            self.assertEqual(len(saved_data), 1)
            self.assertEqual(saved_data[0]['id'], r1.id)
            self.assertEqual(saved_data[0]['width'], r1.width)
            self.assertEqual(saved_data[0]['height'], r1.height)
            self.assertEqual(saved_data[0]['x'], r1.x)
            self.assertEqual(saved_data[0]['y'], r1.y)

    @patch('builtins.open', new_callable=MagicMock)
    def test_load_from_file_file_not_found(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        mock_open.return_value.__enter__.return_value.read.return_value = ""

        # Call the load_from_file method
        result = Rectangle.load_from_file()

        # Assert that open was called with the correct filename
        mock_open.assert_called_once_with('Rectangle.json', 'r', encoding='utf-8')

        # Assert that the result is an empty list
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
