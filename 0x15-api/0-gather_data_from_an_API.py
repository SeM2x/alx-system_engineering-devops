#!/usr/bin/python3
"""for a given employee ID, returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": sys.argv[1]}).json()
    completed = [todo.get("title")
                 for todo in todos if bool(todo.get("completed"))]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
          len(completed), len(todos)))
    [print('\t', todo) for todo in completed]
