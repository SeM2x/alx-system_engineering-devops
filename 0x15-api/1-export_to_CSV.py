#!/usr/bin/python3
"""for a given employee ID, returns information
about his/her TODO list progress."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()
    data = [[sys.argv[1], user.get('username'), todo.get(
        'completed'), todo.get('title')] for todo in todos]
    with open(sys.argv[1] + '.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
