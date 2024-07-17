#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and uses
 the GitHub API to display your id"""


if __name__ == '__main__':
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = "https://api.github.com/user"
    rquest = requests.get(url, auth=auth)
    print(rquest.json().get("id"))
