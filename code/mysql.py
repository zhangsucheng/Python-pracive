import pymysql
from pymysql.cursors import DictCursor


def main():
    con = pymysql.connect(host='192.168.110.40', port=3308,
                          database='micro-crossing', charset='utf8',
                          user='root', password='system')
    try:
        print("================connect mysql================")
        with con.cursor(cursor=DictCursor) as cursor:
            cursor.execute("select * from ops_pole_report")
            results = cursor.fetchall()
            print(results)
            with open("../res/out/crossing.txt","w",encoding="utf-8") as fs:
                fs.write(str(results))
    finally:
        print("=====================end======================")
        con.close()


if __name__ == "__main__":

    main()
