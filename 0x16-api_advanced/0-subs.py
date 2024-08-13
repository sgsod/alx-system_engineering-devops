#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function returns the total number of subscribers of a given subreddit.
    """

    if subreddit is None or isinstance(subreddit, str) is False:
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 127.0.6533.100'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
