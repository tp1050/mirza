import mysql.connector
from mysql.connector import Error
import sys
import MySQLdb


class AnbarBase:

    def __init__(self,host='localhost',user='c',password='22111357',port=3306,database='Moozmar'):
        self.host=host
        self.port=port
        self.database=database
        self.user=user
        self.password=password
        l=vars(self)
        self.conn=mysql.connector.connect(**l)

    @staticmethod
    def mySQLize(s):
        return   MySQLdb.escape_string(s)

    # def gettAnbar(self):
    #     return self.conn
    #
    #
    # def getAnbar(loc='No',secure=0):
    #     if loc=='N0':
    #         loc=Address()
    #     if secure:
    #         return False
    #     l=loc.getLocation()
    #     # print(l)
    #     try:
    #         conn = mysql.connector.connect(**l)
    #         # berin(1,'%')
    #         if conn.is_connected():
    #             print('Connected to MySQL database')
    #             return conn
    #         else:
    #             return None
    #     except Error as e:
    #         sexyError(e)
    # def exec(stmt,conn='NO'):
    #     passed=1
    #     if conn=='NO':
    #         conn = getAnbar()
    #         passed = 0
    #     mc = conn.cursor(buffered=True)
    #     recs="   "
    #     try:
    #         mc.execute(stmt)
    #         conn.commit()
    #         recs=mc.fetchone()
    #     except Exception as e:
    #         sexyError(e)
    #     mc.close()
    #     if not passed:
    #         conn.close()
    #     return recs
    #
    #
    #
    # def begir(tbl,col,cndtion,conn='NO'):
    #     if conn=='NO':
    #         conn = getAnbar()
    #     stmt='select {} from {} where {}="{}";'
    #     stmt2=stmt.format(col,tbl,col,cndtion)
    #     ret=exec(stmt2)
    #     return ret
    # def bezar(tbl,col,val,conn='NO'):
    #     if conn == 'NO':
    #         conn = getAnbar()
    #     stmt='insert into {} ({}) values({});'.format(tbl,col,val)
    #     print (stmt)
    #     return exec(stmt,conn)
    #
    # def getDicID(org,conn='NO'):
    #     res=-1
    #     if conn=='NO':
    #         conn = getAnbar()
    #     stmt = 'select ID,eq from Moozmar.Dictionary where original="{}";'
    #     res=exec(stmt.format(org), conn)
    #     if res is not None:
    #         # print(res)
    #         res=res
    #
    #     else:
    #         exec('insert into Moozmar.Dictionary(original) values("{}");'.format(org),conn)
    #         res=getDicID(org,conn)
    #     return res
    #
    # def getSymID(dicEq,conn = 'NO'):
    #     if conn == 'NO':
    #         conn = getAnbar()
    #     stmt = 'select ID from Moozmar.Deg2Sym where sym="{}";'.format(dicEq)
    #
    #     res = exec(stmt.format(dicEq), conn)
    #     if res is not None:
    #         return res[0]
    #     # print(res)
    #     return -1


