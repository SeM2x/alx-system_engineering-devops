#!/usr/bin/python3
"""
for a given employee ID, returns information
about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    try:
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            user_id)
        user = requests.get(user_url).json()
        user_name = user.get("name")
        todos_url = "https://jsonplaceholder.typicode.com/todos?" \
            "userId={}".format(
                user_id)
        todos = requests.get(todos_url).json()
        tasks = len(todos)
        done_tasks = 0
        for todo in todos:
            if bool(todo.get("completed")):
                done_tasks += 1
        print(f"Employee {user_name} is done with tasks({
              done_tasks}/{tasks}):")
        for todo in todos:
            if bool(todo.get("completed")):
                print(todo.get("title"))

    except Exception:
        print("Error")
