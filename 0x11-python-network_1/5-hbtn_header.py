#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    reqst = requests.get(url)
    print(reqst.headers.get('X-Request-Id'))
