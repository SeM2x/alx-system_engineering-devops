#!/usr/bin/python3
"""
Defines number_of_subscribers(subreddit)
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns
    the number of subscribers for a given subreddit.
    """

    res = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        allow_redirects=False
    )
    if res.status_code == 200:
        data = res.json()
        return int(data.get('data').get('subscribers'))
    else:
        return 0
