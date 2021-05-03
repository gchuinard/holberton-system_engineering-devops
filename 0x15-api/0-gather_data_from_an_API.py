#!/usr/bin/python3
"""
Using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


def main():
    url = 'https://jsonplaceholder.typicode.com/'
    user = sys.argv[1]
    urlId = url + 'users/?id=' + user
    employee = json.loads(requests.get(urlId).text)
    urlId = url + 'todos/?userId=' + user
    totalTasks = json.loads(requests.get(urlId).text)
    urlId = url + 'todos/?userId=' + user + '&completed=true'
    doneTasks = json.loads(requests.get(urlId).text)
    print("Employee {} is done with tasks({}/{}):\
    ".format(employee[0]['name'], len(doneTasks), len(totalTasks)))
    for task in doneTasks:
        print("\t {}".format(task['title']))


if __name__ == "__main__":
    main()
