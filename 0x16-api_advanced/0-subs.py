#!/usr/bin/python3
"""module that define number_of_subscribers(subreddit) function"""
import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API
    and returns the number of subscribers"""
    request = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        allow_redirects=False
    )
    count = request.json().get('data').get('subscribers')
    if count is None:
        return 0
    return count
