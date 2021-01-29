from utils.db import ConnectDatabase

db = ConnectDatabase('ohop')
ib = ConnectDatabase('tuan')

if __name__ == '__main__':
    pass

    sql = "select pid, building_name from tb_union_lottery_result;"
    db.execute(sql)
    for i in db.cursor.fetchall():
        if i[0] != None:
            pid = i[0]
            building_name = i[1]
            tql = "insert into tb_union_lottery_result(pid, building_name) values ('{}','{}');".format(pid,building_name)
            ib.run(tql)
    # ib.close()
    # db.close()