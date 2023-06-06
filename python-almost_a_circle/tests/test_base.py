'''test_base module'''
import unittest
from unittest.mock import patch
from models.base import Base

class TestBase(unittest.TestCase):
    '''TestBase class docstring'''
    def test_id_assignment(self):
        '''test the automatic assignment of incremental ids, and the
        assignment of specific id when provided'''
        base1 = Base()
        base2 = Base()
        base3 = Base(100)

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 100)

    def test_id_type(self):
        '''test the type of id attribute to ensure an integer'''
        base = Base(10)
        self.assertIsInstance(base.id, int)

    def test_to_json_empty(self):
            '''test to_json_string with empty list'''
            self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_None(self):
        '''test to_json_string with None'''
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string_empty(self):
        '''test from_json_string with empty string'''
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_None(self):
        '''test from_json_string with None'''
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_valid(self):
        '''test from_json_string with valid JSON string'''
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_id_assignment_with_string(self):
        '''test the assignment of id attribute with a string'''
        base = Base("string")
        self.assertEqual(base.id, "string")

if __name__ == '__main__':
    unittest.main()
