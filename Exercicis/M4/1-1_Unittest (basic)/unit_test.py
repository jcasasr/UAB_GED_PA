import unittest
from vector import Vector


class TestVector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.empty = Vector([])
        cls.single_element = Vector([1])
        cls.multiple_element = Vector([1, 2, 3])

    def test_str_empty(self):
        self.assertEqual("[]", str(self.empty))

    def test_str_single_element(self):
        self.assertEqual("[1]", str(self.single_element))

    def test_str_multiple_element(self):
        self.assertEqual("[1,2,3]", str(self.multiple_element))
