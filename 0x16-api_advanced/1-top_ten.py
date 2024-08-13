#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    if subreddit is None or isinstance(subreddit, str) is False:
        print("None")

    limit = {'limit' : 10}

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, params=limit)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
