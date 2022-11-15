#!/usr/bin/python3
"""This script makes a request to a REST API"""

import csv
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_data = requests.get("{}/users/{}".format(base_url, id)).json()
    todo_data = requests.get("{}/users/{}/todos".format(base_url, id)).json()
    name = user_data.get('username')

    for value in todo_data:
        # data = '"{}","{}","{}","{}"\n'.format(id,
        #                                       name,
        #                                       value.get('completed'),
        #                                       value.get('title'))
        data = [id, name, value.get('completed'), value.get('title')]
        filename = "{}.csv".format(id)
        with open(filename, 'a', encoding="utf-8") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(data)
            # f.write(data)
