#!/usr/bin/python3
"""number of subscribers for a given subreddit"""

from requests import get
import unittest


def number_of_subscribers(subreddit):
    """
    function returns the total number of subscribers of the subreddit.

    Args:
        subreddit(string): should contain a subreddit

    Return: number of subscribers to the subreddit"""

    if subreddit is None:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url)
    results = response.json()

    if 'kind' in results:
        if results['kind'] != 't5':
            return 0
        else:
            return results.get('data').get('subscribers')
    else:
        return 0


class TestSubs(unittest.TestCase):
    """testing number_of_subscribers"""
    def setUp(self):
        self.number_of_subs = __import__('0-subs').number_of_subscribers

    def test_number_of_subscribers_valid(self):
        existingSub = self.number_of_subs('programming')

        self.assertIsInstance(existingSub, int)

    def test_number_of_subscribers_invalid(self):
        nonexistingSub = self.number_of_subs('johnfixjohnbreakjohnisallbkb')

        self.assertIsInstance(nonexistingSub, int)
        self.assertEqual(nonexistingSub, 0)


if __name__ == "__main__":
    unittest.main()
