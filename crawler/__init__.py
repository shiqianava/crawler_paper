#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from .config import DOWNLOAD_DIR
from .fetch_pdf_url_via_europepmc import fetch_pdf_url_via_europepmc
from .fetch_pdf_url_via_openaccess import fetch_pdf_url_via_openaccess
from .fetch_pdf_url_via_unpaywall import fetch_pdf_url_via_unpaywall
from .fetch_pdf_via_sciencedirect import fetch_pdf_via_sciencedirect
from .fetch_pdf_via_wiley import fetch_pdf_via_wiley
from .units import send_http_get_request

# 确保下载目录存在（但不删除旧文件）
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ---------------------------
# 下载 PDF 主流程
# ---------------------------

# 假设 DOWNLOAD_DIR 已经定义
DOWNLOAD_DIR = 'downloads'

def download_pdf(doi):
    if not doi:
        print(f"[SKIP] 无法获取 DOI：{doi}")
        return False

    # 处理文件名中的非法字符
    safe_doi = doi.replace('/', '-')
    out = os.path.join(DOWNLOAD_DIR, f"{safe_doi}.pdf")
    if os.path.exists(out):
        print(f"[SKIP] 已存在文件：{out}")
        return True

    # 定义返回 URL 的函数列表和返回 PDF 内容的函数列表
    url_fetchers = [
        fetch_pdf_url_via_unpaywall, 
        fetch_pdf_url_via_europepmc,
        fetch_pdf_url_via_openaccess
    ]
    pdf_fetchers = [
        fetch_pdf_via_sciencedirect
    ]

    # 先尝试返回 URL 的函数
    for fetcher in url_fetchers:
        pdf_url = fetcher(doi)
        if not pdf_url:
            continue
        print(f"[INFO] 使用 {fetcher.__name__} 获取到 PDF URL：{pdf_url}")
        try:
            resp = send_http_get_request(pdf_url,  response_type="pdf", stream=True)
            if resp:
                with open(out, 'wb') as f:
                    for chunk in resp:
                        f.write(chunk)
                print(f"[OK] 已下载：{out}")
                return True
            else: 
                print(f"[FAIL] {pdf_url} 未请求到 pdf 数据")
        except Exception as e:
            print(f"[WARN] 下载失败 DOI={doi}: {e}")

    # 再尝试返回 PDF 内容的函数
    for fetcher in pdf_fetchers:
        pdf = fetcher(doi)
        if not pdf:
            continue
        print(f"[INFO] 使用 {fetcher.__name__} 获取到 PDF 内容")
        try:
            with open(out, 'wb') as f:
                f.write(pdf)
            print(f"[OK] 已下载：{out}")
            return True
        except Exception as e:
            print(f"[WARN] 保存失败 DOI={doi}: {e}")
    

    print(f"[FAIL] 无法下载 DOI={doi}")
    return False




