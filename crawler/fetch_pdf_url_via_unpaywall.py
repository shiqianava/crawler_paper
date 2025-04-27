# -*- coding: utf-8 -*-

from .units import send_http_get_request
from .config import UNPAYWALL_EMAIL,UNPAYWALL_URL

def fetch_pdf_url_via_unpaywall(doi):
    api = UNPAYWALL_URL.format(doi=doi, email=UNPAYWALL_EMAIL)
    data = send_http_get_request(api)
    
    if data:
        if data.get("is_oa"):
            loc = data.get("best_oa_location") or {}
            # 'url' 和 'url_for_pdf'都可以作为返回值
            return loc.get("url_for_pdf") or loc.get("url")
        else:
            print(f"该{doi}论文在 Unpaywall 上没有开放获取权限")
    return None