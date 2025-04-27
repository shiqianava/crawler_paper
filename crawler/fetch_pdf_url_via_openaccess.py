# -*- coding: utf-8 -*-

from .units import send_http_get_request
from .config import Open_Access_Button_URL 

# ---------------------------
# Open Access Button网站
# ---------------------------
def fetch_pdf_url_via_openaccess(doi):
    api = Open_Access_Button_URL.format(doi=doi)
    data = send_http_get_request(api)
    if data:
        if data.get("url"):
            return data.get("url")
        else:
            print(f"该{doi}论文在 Open Access Button 上没有开放获取权限")
    return None
