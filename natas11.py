import base64
import requests

from urllib import unquote
from requests.auth import HTTPBasicAuth


def get_key(x, y):
    key = ''
    for c1, c2 in zip(x, y):
        key += chr(ord(c1) ^ ord(c2))

    return key


def xor_encrypt(data):
    key = 'qw8J'
    out = ''

    for i, d in enumerate(data):
        out += chr(ord(d) ^ ord(key[i % len(key)]))

    return out


HOST = "http://natas11.natas.labs.overthewire.org/"
params = dict(bgcolor='#ffffff')

r = requests.get(HOST, params=params, auth=HTTPBasicAuth('natas11', 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'))
print r.url
print r.headers

cookie = r.cookies['data']
original_json = '{"showpassword":"no","bgcolor":"#ffffff"}'
print 'key pattern: ', get_key(base64.b64decode(unquote(cookie)), original_json)

hacky_json = '{"showpassword":"yes","bgcolor":"#ffffff"}'
cookies = dict(data=base64.b64encode(xor_encrypt(hacky_json)))
print 'hacky cookie: ', cookies

r = requests.get(HOST, params=params, auth=HTTPBasicAuth('natas11', 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'), cookies=cookies)
print [line for line in r.content.split('\n') if 'natas12' in line]