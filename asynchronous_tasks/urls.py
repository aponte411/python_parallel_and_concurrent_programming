from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request

URLS = [
    'http://www.foxnews.com/',
    'http://www.cnn.com/',
    'http://europe.wsj.com/',
    'http://www.bbc.co.uk/',
    'http://some-made-up-domain.com/',
]

def load_url(url: str, timeout: int):
    with urllib.request.urlopen(url,timeout=timeout) as conn:
        return conn.read()

def main():
    with ThreadPoolExecutor(max_workers=5) as pool:
        future_to_url = {pool.submit(load_url, url, 60): url for url in URLS}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as e:
                print(f"{url} generated exception {e}")
            print(f"{url} page in bytes {len(data)}")

if __name__ == "__main__":
    main()
