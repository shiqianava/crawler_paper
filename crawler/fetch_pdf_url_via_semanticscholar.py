# -*- coding: utf-8 -*-
import requests
from .units import send_http_get_request

# 该网站的所有接口都不能获取论文的 pdf 链接，已经弃用
def fetch_pdf_url_via_semanticscholar(doi):
    SEMANTIC_SCHOLAR_URL = "https://api.semanticscholar.org/v1/paper/DOI:{doi}"
    url = SEMANTIC_SCHOLAR_URL.format(doi=doi)
    print(url)
    data = send_http_get_request(url)
    print(data)
    if data:
        if data.get("isOpenAccess"):
            print("SEMANTIC_SCHOLAR获取到了一次pdfurl")
            return data.get("pdfUrl")
        else:
            print(f"该{doi}论文在 Semantic Scholar 上没有开放获取权限")
    return None