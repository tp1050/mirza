import mysql.connector
from mysql.connector import Error
import sys
import MySQLdb
from Khadang import *
from DegJet import *


class AnbarBase(DegJet):
    def __init__(self,host='192.168.2.10',user='c',password='22111357',port=3306,database='Moozmar'):
        self.database = database
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        try:
            self.conn=mysql.connector.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database)
            if self.conn.is_connected():
                print('Connected to MySQL database')
            else:
                assert('Be ga raft!!')
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
            if all==0:
                recs=mc.fetchone()
            elif all==1:
                recs=mc.fetchall()
        except Exception as e:
            sexyError(e)
        mc.close()
        return recs


    def begir(self,tbl,col,condtion='',stmt=''):
        if condtion:
            stmt='select {} from {} where {}="{}";'.format(col,tbl,col,condtion)
        else:
            stmt = 'select {} from {};'.format(col,tbl,col)
        ret=self.exec(stmt=stmt)
        return ret
    
    def bezar(self,tbl,col,val):
        stmt='insert into {}({}) values({});'.format(tbl,col,val)
        return self.exec(stmt,all=9)



