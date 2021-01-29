import requests
from lxml import etree

from utils.db import ConnectDatabase
from utils.user_agent import USERAGENT

ua = USERAGENT()
db = ConnectDatabase('ohop')


class Worm(object):
    def __init__(self, num, url):
        self.url = url
        self.num = num
        self.headers = {
            'Cookie': 'Hm_lvt_dc99a9c71f9765d5a29ad86b83069d23=1607087519; Hm_lpvt_dc99a9c71f9765d5a29ad86b83069d23=1607087519',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': ua.user_agent,
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Host':'www.hz-notary.com',
            'Referer':'https://www.hz-notary.com/lottery/detail?lottery.id=8817c16955cf46fa87bcfc13ac954df1',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'same-origin',
            'Sec-Fetch-User':'?1',
            'Upgrade-Insecure-Requests':'1',
}

    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        return response.content

    def parse_data(self, data):
        data = data.decode()
        html = etree.HTML(data)
        value_list = html.xpath('//a[contains(@title, ".pdf")]/@href')
        return value_list

    def save_data(self, url):
        print(self.num)
        if len(url) > 0:
            # sql = "update lottery_yxdj_yhjg set yxdj_down='{}' where id={};".format(url[0], self.num)
            sql = "update lottery_yxdj_yhjg set yhjg_down='{}' where id={};".format(url[0], self.num)
            db.run(sql)
        else:
            # sql = "update lottery_yxdj_yhjg set yxdj_down='{}' where id={};".format('暂无pdf', self.num)
            sql = "update lottery_yxdj_yhjg set yhjg_down='{}' where id={};".format('暂无pdf', self.num)
            db.run(sql)

    def run(self):
        response = self.get_data()
        url = self.parse_data(response)
        self.save_data(url)

        # next_url = self.url
        # while True:
        #     response = self.get_data(next_url)
        #     data_list, next_url = self.parse_data(response)
        #     self.save_data(data_list)
        #     if next_url == None:
        #         break


if __name__ == '__main__':
    # sql = "select id, yxdj_url from lottery_yxdj_yhjg;"
    sql = "select id, yhjg_url from lottery_yxdj_yhjg;"
    db.execute(sql)
    for i in db.cursor.fetchall():
        num = i[0]
        url = i[1]
        # if url == '暂无意向登记':
        if url == '暂无摇号结果':
            continue
        worm = Worm(num, url)
        worm.run()
    db.close()
# url = 'https://www.hz-notary.com/lottery/detail?lottery.id=8817c16955cf46fa87bcfc13ac954df1'
# worm = Worm(2251, url)
# worm.run()