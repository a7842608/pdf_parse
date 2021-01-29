import requests
from lxml import etree

from utils.db import ConnectDatabase
from utils.user_agent import USERAGENT

ua = USERAGENT()
db = ConnectDatabase('ohop')


class Worm(object):
    def __init__(self, num, url):
        self.url = url
        self.num = str(num)
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
        print(self.num)
        r = requests.get(self.url, headers=self.headers, stream=True)
        # filename = r"C:\Users\86138\Desktop\20200905房小团\ohop\parse_pdf\yxdj\{}.pdf".format(self.num + '_yxdj')
        filename = r"C:\Users\86138\Desktop\20200905房小团\ohop\parse_pdf\yhjg\{}.pdf".format(self.num + '_yhjg')
        with open(filename, 'wb+') as f:
            f.write(r.content)


if __name__ == '__main__':
    sql = "select id, yhjg_down from lottery_yxdj_yhjg;"
    # sql = "select id, yxdj_down from lottery_yxdj_yhjg where id between 4400 and 4490;"
    db.execute(sql)
    for i in db.cursor.fetchall():
        num = i[0]
        url = i[1]
        # if url == '暂无意向登记':
        if url == None:
            continue
        elif url == '暂无pdf':
            continue
        worm = Worm(num, url)
        worm.get_data()
    db.close()
