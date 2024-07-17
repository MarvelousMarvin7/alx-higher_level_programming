#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
 the body of the response."""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    rquest = requests.get(url)
    try:
        rquest.raise_for_status()
        print(rquest.text)
    except Exception as e:
        print('Error code: {}'.format(rquest.status_code))
