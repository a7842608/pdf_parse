import pyocr
import importlib
import sys
import time

# from pdfdocument.document import PDFDocument

importlib.reload(sys)
time1 = time.time()
# print("初始时间为：",time1)


# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

import os.path
# from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
# from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

# text_path = r'words-words.pdf'


# text_path = r'photo-words.pdf'

def parse(text_path):
    '''解析PDF文本，并保存到TXT文件中'''
    fp = open(text_path, 'rb')
    # 用文件对象创建一个PDF文档分析器
    parser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()

    # 连接分析器，与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始化密码，如果没有密码，就创建一个空的字符串
    doc.initialize('')

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        pass
        # raise PDFTextExtractionNotAllowed
    else:
        # 创建PDF，资源管理器，来共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释其对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        result = []
        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages():  # doc.get_pages() 获取page列表
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            for x in layout:
                if hasattr(x, "get_text"):
                    result.append(x.get_text().strip())
                    results = x.get_text().strip()
        # print(result)
    time2 = time.time()
    print("总共消耗时间为:", time2 - time1)
    return result


if __name__ == '__main__':
    pass
    # pdf = r'C:\Users\86138\Desktop\20200905房小团\ohop\parse_pdf\yhjg\2252_yhjg.pdf'
    # a = parse(pdf)
