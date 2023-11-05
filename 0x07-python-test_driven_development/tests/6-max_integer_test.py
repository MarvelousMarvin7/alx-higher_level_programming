#!/usr/bin/python3
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for max_integer function"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_docstring(self):
        self.assertIsNotNone(max_integer, __doc__)

    def test_normal_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        # only one element
        self.assertEqual(max_integer([1]), 1)

    def test_neg_int(self):
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
        with self.assertRaises(TypeError):
            max_integer(None)

    if __name__ == "__main__":
        unittest.main()
