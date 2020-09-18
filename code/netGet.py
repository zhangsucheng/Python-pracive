from threading import Thread

import requests


def test():
    res = requests.get("http://127.0.0.1:8006/report/all")
    data = res.json()
    print(data)


def getkey():
    res1 = requests.post("http://192.168.110.236:82/zuul/oauth/",
                         {"username": "tzjj2018",
                          "password": "111111"})
    if res1.status_code == 200:
        cookies = res1.cookies
        print(cookies.get("LESITSID"))
        LESITSID = cookies.get("LESITSID")
        return LESITSID
    else:
        print("login error")
        return False


def main():
    if getkey():
        cookies = dict(LESITSID=str(getkey()))
        res2 = requests.get("http://192.168.110.236:82/zuul/oauth/isLogin", cookies=cookies)
        data2 = res2.json()
        print("====success=====")
        print(data2)


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
