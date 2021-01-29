import requests
from lxml import etree

from utils.db import ConnectDatabase
from utils.user_agent import USERAGENT

ua = USERAGENT()
db = ConnectDatabase('ohop')


class Worm(object):
    def __init__(self,num, url):
        self.num = num
        self.url = url
        self.headers = {
            'Accept-Encoding':' gzip, deflate, br',
            'Accept-Language':' zh-CN,zh;q=0.9',
            'Cache-Control':' max-age=0',
            'Connection':' keep-alive',
            'Host':' www.hz-notary.com',
            'Referer':' https://www.hz-notary.com/lottery/detail?lottery.id=8817c16955cf46fa87bcfc13ac954df1',
            'Sec-Fetch-Dest':' document',
            'Sec-Fetch-Mode':' navigate',
            'Sec-Fetch-Site':' same-origin',
            'Sec-Fetch-User':' ?1',
            'Upgrade-Insecure-Requests':' 1',
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
        yxdj_url = html.xpath('//a[contains(text(), "购房意向登记汇总表")]/@href')
        yhjg_url = html.xpath('//a[contains(text(), "销售摇号结果")]/@href')
        return yxdj_url, yhjg_url

    def save_data(self, yxdj_url, yhjg_url):
        ti = 'https://www.hz-notary.com'

        if len(yxdj_url) > 0:
            yxdj = ti + yxdj_url[0]
        else:
            yxdj = '暂无意向登记'

        if len(yhjg_url) > 0:
            yhjg = ti + yhjg_url[0]
        else:
            yhjg = '暂无摇号结果'

        # sql = "update students set name = '王铁蛋' where id = 6;"
        sql = "update lottery_yxdj_yhjg set yxdj_url='{}', yhjg_url='{}' where id={};".format(yxdj, yhjg, self.num)
        db.run(sql)

        print(yxdj)
        print(yhjg)



    def run(self):
        response = self.get_data()
        a, b = self.parse_data(response)
        self.save_data(a, b)

        # next_url = self.url
        # while True:
        #     response = self.get_data(next_url)
        #     data_list, next_url = self.parse_data(response)
        #     self.save_data(data_list)
        #     if next_url == None:
        #         break


if __name__ == '__main__':
    sql = "select id, url from lottery_yxdj_yhjg;"
    db.execute(sql)
    for i in db.cursor.fetchall():
        num = i[0]
        url = i[1]
        worm = Worm(num, url)
        worm.run()
    db.close()
    # url = 'https://www.hz-notary.com/lottery/detail?lottery.id=8817c16955cf46fa87bcfc13ac954df1'
    # worm = Worm(2251, url)
    # worm.run()