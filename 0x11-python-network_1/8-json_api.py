#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == '__main__':
    import sys
    import requests

    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ""
    payload = {'q': arg}
    url = "http://0.0.0.0:5000/search_user"
    rquest = requests.post(url, data=payload)
    try:
        rquest.raise_for_status()
        json = rquest.json()
        if len(json) == 0:
            print('No result')
        else:
            print("[{:d}] {}".format(json['id'], json['name']))
    except Exception:
        print('Not a valid JSON')
