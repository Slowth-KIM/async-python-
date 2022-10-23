import time
import requests


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10
    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)

        """
        같은 의미
        session = requests.Session()
        session.get(url)
        session.close()"""


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 12
