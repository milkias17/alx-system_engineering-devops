#!/usr/bin/python3
"""Returns information about an employee's TODO list progress"""
import csv
from sys import argv

import requests

if __name__ == "__main__":
    user_id = argv[1]
    employee_id = argv[1]
    url_base = "https://jsonplaceholder.typicode.com"
    todos = requests.get(f"{url_base}/users/{employee_id}/todos").json()
    user = requests.get(f"{url_base}/users/{employee_id}").json()

    with open(f"{user_id}.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile, doublequote=True)
        for todo in todos:
            csvfile.write('"{}",'.format(user.get("id")))
            csvfile.write('"{}",'.format(user.get("username")))
            csvfile.write('"{}",'.format(todo.get("completed")))
            csvfile.write('"{}"\n'.format(todo.get("title")))
