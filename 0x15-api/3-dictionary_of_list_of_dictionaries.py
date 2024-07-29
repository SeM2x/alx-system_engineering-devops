#!/usr/bin/python3
"""for a given employee ID, returns information
about his/her TODO list progress."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    data = {}
    for user in users:
        todos = requests.get(
            url + "/todos", params={"userId": user.get('id')}).json()
        data[user.get('id')] = [{"username": user.get('username'),
                                 "task": todo.get('title'),
                                 "completed": todo.get('completed')}
                                for todo in todos]
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
