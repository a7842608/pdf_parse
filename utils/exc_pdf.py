import pathlib
import pdfplumber
from openpyxl import Workbook

# f_path = r'C:\Users\86138\Desktop\20200905房小团\pdf_parse\yxdj\2251_yxdj.pdf'
# out_path = '002pdf_excel.xlsx'

# with pdfplumber.open(pdf) as p:
#     first_page = p.pages[0]
#     tables = first_page.extract_tables()
#     for table in tables:
#         df = pd.DataFrame(table)
#         第一列当成表头：
        # df = pd.DataFrame(table[1:], columns=table[0])
        # print(df)


def pase_exc(f_path, out_path):
    wb = Workbook()
    sheet = wb.active
    with pdfplumber.open(f_path) as pdf:
        i = len(pdf.pages)
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            table = page.extract_table()
            try:
                for row in table:
                    sheet.append(row)
            except:
                print(f_path)
                continue
        wb.save(out_path)

# 2792 2810 2838 2839 2894 2897