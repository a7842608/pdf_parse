import requests

# //a[contains(text(), "购房意向登记汇总表")]/@href
# //a[contains(text(), "销售摇号结果")]/@href


import requests
from lxml import etree

from utils.db import ConnectDatabase
from utils.user_agent import USERAGENT

ua = USERAGENT()
# print(a.user_agent)
db = ConnectDatabase('ohop')

class Worm(object):
    def __init__(self, page):
        self.url = 'https://www.hz-notary.com/lottery/index?page.pageNum={}'.format(page)
        self.headers = {
            'Cookie': 'Hm_lvt_dc99a9c71f9765d5a29ad86b83069d23=1607087519; Hm_lpvt_dc99a9c71f9765d5a29ad86b83069d23=1607087519',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': ua.user_agent
        }

    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        return response.content

    def parse_data(self, data):
        data = data.decode()
        html = etree.HTML(data)
        value_list = html.xpath('//li/div/a/@href')
        title = html.xpath('//li/div/a/text()') # title
        return value_list, title

    def save_data(self, url, title_v):
        # https://www.hz-notary.com/lottery/index?page.pageNum=1
        title = 'https://www.hz-notary.com' # lottery/detail?lottery.id=8817c16955cf46fa87bcfc13ac954df1
        a = [title + i for i in url]
        b = [i.replace('\r\n\t\t\t\t\t\t\t', '') for i in title_v]
        for aa, bb in zip(a, b):
            sql = "insert into lottery_yxdj_yhjg (url, name) values ('{}', '{}')".format(aa, bb)
            db.run(sql)

    def run(self):
        response = self.get_data()
        url, title = self.parse_data(response)
        self.save_data(url, title)

        # next_url = self.url
        # while True:
        #     response = self.get_data(next_url)
        #     data_list, next_url = self.parse_data(response)
        #     self.save_data(data_list)
        #     if next_url == None:
        #         break


if __name__ == '__main__':
    for i in range(1, 225):
        print('当前第{}页'.format(i))
        worm = Worm(i)
        worm.run()
    db.close()
    # worm = Worm(1)
    # worm.run()
