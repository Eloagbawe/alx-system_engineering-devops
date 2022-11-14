#!/usr/bin/python3
"""This script makes a request to a REST API"""

import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_data = requests.get("{}/users/{}".format(base_url, id)).json()
    todo_data = requests.get("{}/users/{}/todos".format(base_url, id)).json()
    name = user_data.get('username')

    data = []
    data_dict = {}
    for value in todo_data:
        res_dict = {}
        res_dict['task'] = value.get('title')
        res_dict['completed'] = value.get('completed')
        res_dict['username'] = name
        data.append(res_dict)

    data_dict[id] = data

    filename = "{}.json".format(id)
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(json.dumps(data_dict))
