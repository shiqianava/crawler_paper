# request_headers.py
from fake_useragent import UserAgent

ua = UserAgent()

def request_headers(request_type='json', referer=None, cookies=None):
    headers = {
        'User-Agent': ua.random,
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    if request_type == 'html':
        headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
    elif request_type == 'json':
        headers['Accept'] = 'application/json'
    elif request_type == 'pdf':
        headers['Accept'] = 'application/pdf'
        headers['amsRedirect'] = True
    else:
        headers['Accept'] = '*/*'

    if referer:
        headers['Referer'] = referer
    if cookies:
        headers['Cookie'] = cookies

    return headers