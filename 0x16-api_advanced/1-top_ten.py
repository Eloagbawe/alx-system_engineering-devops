#!/usr/bin/python3
"""This script queries the REDDIT API"""

import requests


def top_ten(subreddit):
    """
    This function prints the titles of the first
    10 hot posts listed for a given subreddit.
    """
    base_url = 'https://www.reddit.com'
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus\
                5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/107.0.0.0 Mobile Safari/537.36'}

    data = requests.get("{}/r/{}/hot.json"
                        .format(base_url, subreddit), headers=headers,
                        allow_redirects=False)
    if data.status_code != 200:
        print(None)
    else:
        result = data.json().get('data').get('children')
        for i in range(0, 10):
            print(result[i].get('data').get('title'))
