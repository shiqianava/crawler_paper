# -*- coding: utf-8 -*-

from .units import send_http_get_request
from .config import CROSSREF_URL

def fetch_pdf_url_via_crossref(doi):
    api = CROSSREF_URL.format(doi=doi)
    data = send_http_get_request(api)
    if data:
        links = data.get('message', {}).get('link', [])
        for link in links:
            if link.get('content-type') == 'application/pdf':
                # print(link.get('URL'))
                return link.get('URL')
            else:
                print(f"该{doi}论文在 Crossref 上没有相关链接")
    return None