# -*- coding: utf-8 -*-

import requests
from .request_headers import request_headers

import requests


def request_headers():
    # 这里可以根据实际情况定义请求头
    return {'Accept': 'application/json'}


def send_http_get_request(url, headers=request_headers(), timeout=15, response_type='json', max_retries=2, stream=False):
    retries = 0
    while retries < max_retries:
        try:
            r = requests.get(url, headers=headers, timeout=timeout, stream=stream)
            r.raise_for_status()
            if response_type == 'json':
                if stream:
                    print("[WARN] 不建议对 JSON 响应使用流式模式。")
                return r.json()
            elif response_type == 'text':
                if stream:
                    return r.iter_lines()
                return r.text
            elif response_type == 'pdf':
                
                if stream:
                    return r.iter_content(chunk_size=8192)
                return r.content
        except requests.exceptions.Timeout:
            print(f"[WARN] 请求 {url} 时超时，第 {retries + 1} 次重试")
            retries += 1
        except requests.exceptions.HTTPError as http_err:
            print(f"[ERROR] 请求 {url} 时出现 HTTP 错误: {http_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"[ERROR] 请求 {url} 时出现请求异常: {req_err}")
            return None
        except ValueError as json_err:
            if response_type == 'json':
                print(f"[ERROR] 解析 {url} 的响应为 JSON 时出错: {json_err}")
            return None
    print(f"[ERROR] 请求 {url} 失败，已达到最大重试次数 {max_retries}")
    return None