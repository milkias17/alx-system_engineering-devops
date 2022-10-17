#!/usr/bin/python3
"""Returns information about an employee's TODO list progress"""
import json
from sys import argv

import requests

if __name__ == "__main__":
    employee_id = argv[1]
    url_base = "https://jsonplaceholder.typicode.com"
    todos = requests.get(f"{url_base}/users/{employee_id}/todos").json()
    user = requests.get(f"{url_base}/users/{employee_id}").json()

    tasks = []
    for todo in todos:
        todo_dict = {}
        todo_dict["task"] = todo.get("title")
        todo_dict["completed"] = todo.get("completed")
        todo_dict["username"] = user.get("username")
        tasks.append(todo_dict)
    with open(f"{employee_id}.json", "w") as json_file:
        json_dict = {user.get("id"): tasks}
        json.dump(json_dict, json_file)
