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
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url, allow_redirects=False,
                       headers={"User-Agent": "Custom"},)
    if res.status_code == 200:
        data = res.json()
        return data.get('data').get('subscribers')
    else:
        return 0
