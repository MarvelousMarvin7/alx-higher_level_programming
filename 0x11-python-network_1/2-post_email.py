#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed
 URL with the email as a parameter, and displays the body of the response
 (decoded in utf-8)
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    value = {'email' : sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    reqst = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(reqst) as response:
        print(response.read().decode('utf-8'))
