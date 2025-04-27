# -*- coding: utf-8 -*-

from .units import send_http_get_request
from .config import SCIENCE_DIRECT_URL


# ---------------------------
# Sciencedirect 网站
# ---------------------------
def fetch_pdf_via_sciencedirect(doi):
    headers = {
        "Accept": "application/json",
        "X-ELS-APIKey": "12a8eb40c97addbf7e1aa5ac939c7bdb",
    }
    api = SCIENCE_DIRECT_URL.format(doi=doi)
    data = send_http_get_request(api, headers, response_type="json")
    if data:
        openaccessArticle = data.get("full-text-retrieval-response").get("coredata").get("openaccessArticle")
        if openaccessArticle:
            # 有开放下载权限，直接下载
            headers["Accept"] = "application/pdf"
            pdf = send_http_get_request(api, headers, response_type="pdf")
            return pdf
        else:
            print(f"该{doi}论文在 Science direct 上没有开放获取权限")
    return None