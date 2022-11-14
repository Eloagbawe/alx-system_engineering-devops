#!/usr/bin/python3
"""This script makes a request to a REST API"""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_data = requests.get("{}/users/".format(base_url)).json()

    data_dict = {}
    for value in user_data:
        data = []
        name = value.get('username')
        id = value.get('id')
        todo_data = requests.get("{}/users/{}/todos"
                                 .format(base_url, id)).json()
        for value in todo_data:
            res_dict = {"username": name, "task": value.get("title"),
                        "completed": value.get('completed')}
            data.append(res_dict)
        data_dict[id] = data

    filename = "todo_all_employees.json"
    with open(filename, 'w') as f:
        f.write(json.dumps(data_dict))
