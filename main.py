from crawler.config import DOIS_FILE
from crawler import download_pdf


# ---------------------------
# 主流程：批量处理
# ---------------------------
if __name__ == "__main__":
    # 读取 dois.txt
    try:
        with open(DOIS_FILE, 'r') as f:
            dois = [l.strip() for l in f if l.strip()]
    except FileNotFoundError:
        print(f"[ERROR] 找不到 {DOIS_FILE}")
        exit(1)

    failures = []
    for doi in dois:
        if not download_pdf(doi):
            failures.append(doi)

    if failures:
        with open("failed_downloads.txt", "w") as f:
            for doi in failures:
                f.write(doi + "\n")
        print(f"[DONE] 部分文献下载失败，详情见 failed_downloads.txt")
    else:
        print("[DONE] 全部文献下载完成！")
