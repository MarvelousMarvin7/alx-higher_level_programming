#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    reqst = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(reqst.text)))
    print('\t- content: {}'.format(reqst.text))
