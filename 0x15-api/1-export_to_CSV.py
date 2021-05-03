#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
and export data in the CSV format.
"""
import csv
import json
import requests
from sys import argv


def main():
    url = 'https://jsonplaceholder.typicode.com/'
    user = sys.argv[1]
    urlId = url + 'users/?id=' + user
    employee = json.loads(requests.get(urlId).text)
    urlId = url + 'todos/?userId=' + user
    totalTasks = json.loads(requests.get(urlId).text)

    dataFile = open(userId + '.csv', 'w')
    csvWriter = csv.writer(dataFile, quoting=csv.QUOTE_ALL)

    for task in totalTasks:
        row = []
        row.append(str(user))
        row.append(employee[0]['username'])
        row.append(task['completed'])
        row.append(task['title'])
        csvWriter.writerow(row)
    dataFile.close()


if __name__ == "__main__":
    main()
