# coding=utf-8
import pymysql

# 增删改

file = open(r'C:\Users\86138\Desktop\2020.9.5房小团小程序\一房一价修改版\test\log.text', 'a+', encoding='utf-8')


class ConnectDatabase(object):
    '''连接数据库'''
    def __init__(self, database):
        # 创建连接对象
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='mysql', database=database, charset='utf8')
        # 获取游标对象
        self.cursor = self.conn.cursor()

    def execute(self, statement):
        try:
            # 添加 SQL 语句
            # sql = "insert into students(name) values('刘璐'), ('王美丽');"
            sql = statement
            # 删除 SQ L语句
            # sql = "delete from students where id = 5;"
            # 修改 SQL 语句
            # sql = "update students set name = '王铁蛋' where id = 6;"
            # 执⾏ SQL 语句
            row_count = self.cursor.execute(sql)
            print("SQL 语句执⾏影响的⾏数%d" % row_count)
            # 提交数据到数据库
            self.conn.commit()
            print('数据提交成功')

        except Exception as e:
            print('数据执行错误: ', e)
            # 回滚数据， 即撤销刚刚的SQL语句操作
            self.conn.rollback()
            file.write(statement + '\n')

    def close(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()

    def run(self, data):
        self.execute(data)
        # self.close()


if __name__ == '__main__':
    pass
    # d = 'ohop' # 表名
    # sql = "insert into ohop_content(name) values('刘璐'), ('王美丽');" # 执行语句
    # db = ConnectDatabase(d)
    # db.run(sql)

# sql = "select id, url from m_ke where id BETWEEN 2502 AND 2511;"
#     db.execute(sql)
#     for i in db.cursor.fetchall():
#         print(1, i, type(i))
        # url = i[1]
        # num = i[0]