from threading import Thread

import requests


def main():
    res = requests.get("http://127.0.0.1:8006/hello")
    print(res)


class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/Hao/' + filename, 'wb') as f:
            f.write(resp.content)


if __name__ == '__main__':
    main()