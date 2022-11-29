#!/usr/bin/python3
"""This script queries the REDDIT API"""

import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for
    a given subreddit.
    """
    base_url = 'https://www.reddit.com'
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus\
                5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/107.0.0.0 Mobile Safari/537.36'}

    data = requests.get("{}/r/{}/about.json"
                        .format(base_url, subreddit), headers=headers,
                        allow_redirects=False)
    if data.status_code != 200:
        return 0
    return data.json().get('data').get('subscribers')
