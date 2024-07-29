#!/usr/bin/python3
"""for a given employee ID, returns information
about his/her TODO list progress."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()
    data = {sys.argv[1]: [{"task": todo.get('title'), "completed": todo.get(
        'completed'), "username": user.get('username'), } for todo in todos]}
    with open(sys.argv[1]+'.json', 'w') as file:
        json.dump(data, file)
