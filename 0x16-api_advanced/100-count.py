#!/usr/bin/python3
"""This script queries the REDDIT API"""

import requests


def convertToDict(word_list):
    """This function converts the word list array
    to a dictionary with initialized values
    """
    values = []
    word_list = [x.lower() for x in word_list]
    for a in word_list:
        values.append(0)
    my_dict = dict(zip(word_list, values))

    return my_dict


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
    try:
        result_data = data.json()
        if data.status_code != 200:
            raise Exception
    except Exception:
        print("")
        return
    # if data.status_code != 200:
    #     print("")
    #     return
    result = result_data.get('data')
    hot_posts = result.get('children')
    nextPage = result.get('after')
    if converted_list == {}:
        converted_list = convertToDict(word_list)
    for i in hot_posts:
        title = i.get('data').get('title').lower()
        title_list = title.split()
        word_list = [x.lower() for x in word_list]
        for x in title_list:
            for y in word_list:
                if y == x:
                    converted_list[y] += 1

    if nextPage is None:
        if len(converted_list) == 0:
            print("")
            return
        sorted_list = sorted(converted_list.items(),
                             key=lambda x: (-x[1], x[0]))
        for i in sorted_list:
            if i[1] != 0:
                print("{}: {}".format(i[0], i[1]))
    else:
        count_words(subreddit, word_list, nextPage, converted_list)
