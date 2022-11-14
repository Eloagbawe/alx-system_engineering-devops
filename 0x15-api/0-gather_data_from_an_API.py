#!/usr/bin/python3
"""This script makes a request to a REST API"""

import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_data = requests.get("{}/users/{}".format(base_url, id)).json()
    todo_data = requests.get("{}/users/{}/todos".format(base_url, id)).json()

    name = user_data.get('name')
    task_length = len(todo_data)
    completed_tasks = []

    for value in todo_data:
        if value.get('completed'):
            completed_tasks.append(value.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(completed_tasks), len(todo_data)))

    for value in completed_tasks:
        print("\t {}".format(value))
