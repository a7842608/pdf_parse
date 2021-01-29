import os
import re

from utils.db import ConnectDatabase
from utils.exc_pdf import pase_exc
from utils.utils import parse

db = ConnectDatabase('ohop')

'''
:param
意向登记入库
'''


class ParsePdfFiles(object):
    '''pdf解析'''
    def __init__(self):
        # self.
        pass

    def readfile(self):
        rootdir = r'.\yxdj'
        list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
        for i in range(0, len(list)):
        # for i in range(3, 4):
            pos = os.path.join(rootdir, list[i])
            # print(pos)
            if os.path.isfile(pos):
                # 你想对文件的操作
                pt = os.path.abspath(pos)
                # print(pt)
                basename = os.path.basename(pos)
                name_id = basename.split('_')[0]
                # print(name_id)
    # def pase(self):
    #             pdf = r'.\yxdj\2251_yxdj.pdf'
                out_path = r'C:\Users\86138\Desktop\20200905房小团\pdf_parse\yhjg\{}_yxdj.xlsx'.format(name_id)
                # out_p = r'C:\Users\86138\Desktop\20200905房小团\pdf_parse\yhjg'
                bb = pase_exc(pt, out_path)
                print(name_id)
        # d = []
        # [d.append(i.replace('\n', ';')) for i in bb]
        #
        # print(d)

                # for i in bb:
        #     a = i.replace('\n', ';')
        #     b = ''.join(a)
        #     print(b)

        # xuha = []
        # djha = []
        # for i in bb:
        #     if i == '序号':
        #         continue
        #     if i == '购房登记号':
        #         continue
        #     a = i.replace('\n', ';')
        #     contain_en = re.search('[A-Z]', a)
        #     if contain_en is None:
        #         b = a.split(';')
        #         [djha.append(i) for i in b]
        #     else:
        #         c = a.split(';')
        #         [xuha.append(i) for i in c]

        # print(xuha)
        # print(djha)
        # for aa, bb in zip(djha, xuha):
        #     print(aa, bb)
            # sql = "insert into yaohaojieguo(pid, shunxu, code) values('{}','{}','{}');".format(name_id, aa, bb)
            # db.run(sql)

    # def run(self):
    #     self.readfile()


if __name__ == '__main__':
    pdf = r'C:\Users\86138\Desktop\20200905房小团\ohop\parse_pdf\yxdj\2251_yxdj.pdf'
    # pdf = r'.\yhjg\2252_yhjg.pdf'
    # bb = parse(basename)
    # print(readfile())
    # insertsql(name_id)

    w = ParsePdfFiles()
    w.readfile()
    # db.close()
