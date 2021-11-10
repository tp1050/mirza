import mysql.connector
from mysql.connector import Error
import sys
import MySQLdb
from Khadang import *


class AnbarBase:

    def __init__(self,host='192.168.2.10',user='c',password='22111357',port=3306,database='Moozmar'):
        self.host=host
        self.port=port
        self.database=database
        self.user=user
        self.password=password
        try:
            self.conn=mysql.connector.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database)
        except Error as e :
            sexyError(e)
            
            
    @staticmethod
    def mySQLize(s):
        return   MySQLdb.escape_string(s)

    def exec(self,stmt,all=0):

        mc = self.conn.cursor(buffered=True)
        recs="   "
        try:
            mc.execute(stmt)
            self.conn.commit()
            if all:
                recs=mc.fetchone()
            else:
                recs=mc.fetchall()
        except Exception as e:
            sexyError(e)
        mc.close()
        if not passed:
            conn.close()
        return recs
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


