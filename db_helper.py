from utils.db import ConnectDatabase

db = ConnectDatabase('ohop')
ib = ConnectDatabase('tuan')


class DBHelper(object):
    '''上传数据'''
    def upload(self):
        # sql = "insert into tb_union_lottery_result(pid, building_name) values('{}','{}');".format()

        # sql = "select id, name from lottery_yxdj_yhjg;"
        # sql = "select pid, shunxu, code from yaohaojieguo where id between 169689 and 977822;"
        sql = "select pid, shunxu, gfdengjihao, gfrxingming, goufangrenID,jiatingleixing,bianhao,qitarenxingming,qitarenID from yixiangdengji;"
        db.execute(sql)
        for i in db.cursor.fetchall():
            if i[0] != None:
                pid = i[0]
                shunxu = i[1]
                gfdengjihao = i[2]
                gfxingming = i[3]
                goufangrenID = i[4]
                jiatingleixing = i[5]
                bianhao = i[6]
                qitarenxingming = i[7]
                qitarenID = i[8]
                # tql = "insert into tb_lottery_result(pid, serial_number, buy_house_number) values('{}','{}','{}');".format(num, bd_name, cd)
                tql = "insert into tb_told_purpose(pid, shunxu, buy_house_number,lottery_name, ID_number,house_classfiy,find_number,other_lottery_name,other_ID_number) values('{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(pid, shunxu,gfdengjihao,gfxingming,goufangrenID,jiatingleixing,bianhao,qitarenxingming,qitarenID)

                ib.run(tql)
        db.close()
        ib.close()


if __name__ == '__main__':
    d = DBHelper()
    d.upload()