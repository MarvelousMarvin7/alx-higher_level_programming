#!/usr/bin/python3
"""list 10 recents commits from a github repo"""


if __name__ == '__main__':
    import sys
    import requests

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    rquest = requests.get(url)
    commits = rquest.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"), commits[i].get(
                "commit").get("author").get("name")))
    except IndexError:
        pass
