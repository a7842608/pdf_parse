import shutil

import requests

from down_loadpdf import ua

requests_pdf_url = "http://down.hz-notary.com:10006/pdf/2020/1204/201204144706067_23430144226072055.pdf"

headers = {
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

# //a[contains(@title, ".pdf")]/@href

r = requests.get(requests_pdf_url, headers=headers, stream=True)
filename = "test.pdf"
with open(filename, 'wb+') as f:
    f.write(r.content)
# post_param = {'action': '', 'start': '0', 'limit': '1'}
# r = requests.get(requests_pdf_url, data=post_param, verify=False)
# with open('aaa.pdf', 'wb') as fd:
#     for chunk in r.iter_content(2000):
#         fd.write(chunk)


# r.raw.decode_content = True
# with open("file_name.pdf", 'wb') as f:
#         shutil.copyfileobj(r.raw, f)