#!/usr/bin/python3

"""
    This module requests data from a RESTful API
    (https://jsonplaceholder.typicode.com/)
    and returns information about an all employees
    in JSON format
"""

import json
import requests


def main():
    """ fetches the todo list progress for an employee """
    url_base = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{url_base}/users").json()
    todos = requests.get(f"{url_base}/todos").json()
    json_dict = {}
    for user in users:
        user_todos = []
        for todo in filter(lambda x: x.get('userId') == user.get("id"), todos):
            todo_dict = {}
            todo_dict["username"] = user.get("username")
            todo_dict["task"] = todo.get("title")
            todo_dict["completed"] = todo.get("completed")
            user_todos.append(todo_dict)
        json_dict[user.get("id")] = user_todos

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(json_dict, json_file)


if __name__ == "__main__":
    main()
