#!/usr/bin/python3
"""This script queries the REDDIT API"""

import requests


def count_words(subreddit, word_list, after="", converted_list={}):
    """
     This function parses the title of all hot articles,
     and prints a sorted count of given keywords (case-insensitive,
     delimited by spaces
    """
    base_url = 'https://www.reddit.com'
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus\
                5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/107.0.0.0 Mobile Safari/537.36'}

    data = requests.get("{}/r/{}/hot.json?after={}&limit=100"
                        .format(base_url, subreddit, after),
                        headers=headers, allow_redirects=False)

    if data.status_code != 200:
        return
    result = data.json().get('data')
    hot_posts = result.get('children')
    nextPage = result.get('after')

    # if converted_list == {}:
    #     word_list = [word.lower() for word in word_list]
    #     values = [0 for x in word_list]
    #     converted_list = dict(zip(word_list, values))

    for i in hot_posts:
        title_list = i.get('data').get('title').lower().split()
        for word in word_list:
            lowerCase = word.lower()
            times = len([x for x in title_list if x == lowerCase])
            if converted_list.get(lowerCase) is None:
                converted_list[lowerCase] = times
            else:
                converted_list[lowerCase] += times
            # converted_list[word] += times

    if nextPage is None:
        if len(converted_list) == 0:
            return
        sorted_list = sorted(converted_list.items(),
                             key=lambda x: (-x[1], x[0]))
        [print("{}: {}"
               .format(key, val)) for key, val in sorted_list if val != 0]
    else:
        count_words(subreddit, word_list, nextPage, converted_list)
