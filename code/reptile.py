# 引入模块
import re

import res as res
from bs4 import BeautifulSoup
import requests

# 代理客户端列表
from numpy import random, math

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]


# 创建请求头信息
def create_headers():
    headers = dict()
    headers["User-Agent"] = random.choice(USER_AGENTS)
    headers["Referer"] = "http://www.ke.com"
    return headers


# 定义变量
proxys_src = []
proxys = []


# 请求获取代理地址
def spider_proxyip(num=10):
    try:
        url = 'http://www.xicidaili.com/nt/1'
        # 获取代理 IP 列表
        req = requests.get(url, headers=create_headers())
        source_code = req.content
        # 解析返回的 html
        soup = BeautifulSoup(source_code, 'lxml')
        # 获取列表行
        ips = soup.findAll('tr')

        # 循环遍历列表
        for x in range(1, len(ips)):
            ip = ips[x]
            tds = ip.findAll("td")
            proxy_host = "{0}://".format(tds[5].contents[0]) + tds[1].contents[0] + ":" + tds[2].contents[0]
            proxy_temp = {tds[5].contents[0]: proxy_host}
            # 添加到代理池
            proxys_src.append(proxy_temp)
            if x >= num:
                break
    except Exception as e:
        print("获取代理地址异常:")
        print(e)


# 新房对象
class NewHouse(object):
    def __init__(self, xiaoqu, price, total):
        self.xiaoqu = xiaoqu
        self.price = price
        self.total = total

    def text(self):
        return self.xiaoqu + "," + \
                self.price + "," + \
                self.total

# 创建文件准备写入
def record_data():
    with open("../res/out/newhouse.txt", "w", encoding='utf-8') as f:
        # 获得需要的新房数据
        total_page = 1
        loupan_list = list()
        page = 'http://bj.fang.ke.com/loupan/'
        # 调用请求头
        headers = create_headers()
        # 请求 url 并返回结果
        response = requests.get(page, timeout=10, headers=headers)
        html = response.content
        # 解析返回 html
        soup = BeautifulSoup(html, "lxml")

        # 获取总页数
        try:
            page_box = soup.find_all('div', class_='page-box')[0]
            matches = re.search('.*data-total-count="(\d+)".*', str(page_box))
            total_page = int(math.ceil(int(matches.group(1)) / 10))
        except Exception as e:
            print(e)

        print('总页数：' + str(total_page))
        # 配置请求头
        headers = create_headers()
        # 从第一页开始遍历
        for i in range(1, total_page + 1):
            page = 'http://bj.fang.ke.com/loupan/pg{0}'.format(i)
            print(page)
            response = requests.get(page, timeout=10, headers=headers)
            html = response.content
            # 解释返回结果
            soup = BeautifulSoup(html, "lxml")

            # 获得小区信息
            house_elements = soup.find_all('li', class_="resblock-list")
            # 循环遍历获取想要的元素
            for house_elem in house_elements:
                price = house_elem.find('span', class_="number")
                desc = house_elem.find('span', class_="desc")
                total = house_elem.find('div', class_="second")
                loupan = house_elem.find('a', class_='name')

                # 开始清理数据
                try:
                    price = price.text.strip() + desc.text.strip()
                except Exception as e:
                    price = '0'

                loupan = loupan.text.replace("\n", "")
                # 继续清理数据
                try:
                    total = total.text.strip().replace(u'总价', '')
                    total = total.replace(u'/套起', '')
                except Exception as e:
                    total = '0'

                # 作为对象保存到变量
                loupan = NewHouse(loupan, price, total)
                print(loupan.text())
                # 将新房信息加入列表
                loupan_list.append(loupan)

        # 循环获取的数据并写入到文件中
        for loupan in loupan_list:
            f.write(loupan.text() + "\n")


if __name__ == "__main__":
    record_data()