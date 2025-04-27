# -*- coding: utf-8 -*-

from .units import send_http_get_request
from .config import Europe_PMC_URL


def fetch_pdf_url_via_europepmc(doi):
    url = Europe_PMC_URL.format(doi=doi)
    data = send_http_get_request(url)
    
    if data:
        items = data.get("resultList", {}).get("result", [])
        if items:
            if items[0].get("isOpenAccess") == "N":
                print(f"该{doi}论文在 Europe PMC 上没有开放获取权限")
            else:
                for loc in items[0].get("fullTextUrlList", {}).get("fullTextUrl", []):
                    if loc.get("documentStyle") == "pdf" and loc.get("url"):
                        return loc["url"]
    return None