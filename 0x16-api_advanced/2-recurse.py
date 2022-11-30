#!/usr/bin/python3
"""This script queries the REDDIT API"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    This function returns a list containing the
    titles of all hot articles for a given subreddit.
    """
    base_url = 'https://www.reddit.com'
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus\
                5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/107.0.0.0 Mobile Safari/537.36'}
    # params = {"after": after, "limit": 100}

    data = requests.get("{}/r/{}/hot.json?after={}&limit=100"
                        .format(base_url, subreddit, after),
                        headers=headers, allow_redirects=False)
    if data.status_code != 200:
        return None

    result = data.json().get('data')
    hot_posts = result.get('children')
    nextPage = result.get('after')
    for i in hot_posts:
        hot_list.append(i.get('data').get('title'))

    if nextPage is not None:
        recurse(subreddit, hot_list, nextPage)
    return hot_list
