#!/usr/bin/python3
"""number of subscribers for a given subreddit"""

from requests import get


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
