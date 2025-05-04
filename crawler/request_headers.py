# request_headers.py
from fake_useragent import UserAgent

ua = UserAgent()

def request_headers(response_type='json', referer=None, cookies=None):
    # 动态生成随机的 User-Agent
    user_agent = ua.random

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',  # 添加常见的压缩编码支持
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',  # 表示请求的目标类型
        'Sec-Fetch-Mode': 'navigate',  # 表示请求的模式
        'Sec-Fetch-Site': 'same-origin',  # 表示请求的来源站点
        'Sec-Fetch-User': '?1',  # 表示是否由用户主动发起的请求
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': user_agent  # 使用动态生成的 User-Agent
    }

    if response_type == 'html':
        headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
    elif response_type == 'json':
        headers['Accept'] = 'application/json'
    elif response_type == 'pdf':
        headers['Accept'] = 'application/pdf'
    else:
        headers['Accept'] = '*/*'

    if referer:
        headers['Referer'] = referer
    if cookies:
        headers['Cookie'] = cookies

    return headers