#!/usr/bin/python3
"""Test if 0-subs provides accurate responses"""

import unittest


class myTestCase(unittest.TestCase):
    """testing number_of_subscribers"""
    def setUp(self):
        self.number_of_subscribers = __import__('0-subs').number_of_subscribers

    def test_number_of_subscribers_valid(self):
        existingSub = self.number_of_subscribers('programming')

        self.assertIsInstance(existingSub, int)


    def test_number_of_subscribers_invalid(self):
        nonexistingSub = self.number_of_subscribers('johnfixjohnbreakjohnisaheadache')

        self.assertIsInstance(nonexistingSub, int)
        self.assertEqual(nonexistingSub, 0)
"""
if __name__ == "__main__":
    unittest.main()
"""
