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

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
