import requests
from bs4 import BeautifulSoup

def test_request(url,retry=5):
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"
    }

    try:
        response=requests.get(url=url,headers=headers)
        print(f"[+] {url} {response.status_code}")
    except Exception as exc:
        if retry:
            print(f"[INFO] retry={retry} =>{url}")
            return test_request(url,retry=(retry-1))
        else:
            raise
    else:
        return response

if __name__ == '__main__':
    with open("books_urls.txt","r",encoding="utf-8") as file:
        books_urls=file.read().splitlines()


    for book_url in books_urls:
        try:
            r=test_request(url=book_url)
            soup=BeautifulSoup(r.text,"lxml")
            print(f"{soup.titke.text}")
        except Exception:
            continue
