import unittest

from .flatten import flatten


class TestFlatten(unittest.TestCase):
    def test_one_level_nesting(self):
        nested = [1, 2, [3], 4]
        self.assertEqual(flatten(nested), [1, 2, 3, 4])

    def test_two_level_nesting(self):
        nested = [1, 2, [3, [5, 6]], 4]
        self.assertEqual(flatten(nested), [1, 2, 3, 5, 6, 4])

    def test_list_with_non_int(self):
        nested = [1, 2, 3, ["hello", "world"], 4, 5, ["jeez", 1, [4, 5]]]
        self.assertEqual(flatten(nested), [1, 2, 3, 4, 5, 1, 4, 5])


if __name__=='__main__':
    unittest.main()
