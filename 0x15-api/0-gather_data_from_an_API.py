#!/usr/bin/python3
"""Returns information about an employee's TODO list progress"""
from sys import argv

import requests

if __name__ == "__main__":
    employee_id = argv[1]
    url_base = "https://jsonplaceholder.typicode.com"
    todos = requests.get(f"{url_base}/users/{employee_id}/todos").json()
    user = requests.get(f"{url_base}/users/{employee_id}").json()

    completed_todos = []
    num_completed = 0

    for todo in todos:
        if todo.get("completed"):
            num_completed += 1
            completed_todos.append(todo)

    print(
        f"Employee {user.get('name')} is done with tasks"
        f"({num_completed}/{len(todos)}):")

    for todo in completed_todos:
        print(f"\t {todo.get('title')}")
