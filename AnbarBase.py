import numbers

import mysql.connector
from mysql.connector import ProgrammingError
import sys
# import MySQLdb
from Khadang import *
from DegJet import *


class AnbarBase(DegJet):
    def __init__(self,host='192.168.5.17',user='c',password='22111357',port=3306,database='Moozmar'):
        super().__init__()
        self.stmtSlctCndt = 'SELECT {COLNAMES} from {TABLE} where {COLNAMES}={CONDITION};'
        self.stmtSlctNoCndt = 'select {COLNAMES} from {TABLE};'
        self.insrtStmt = 'INSERT INTO {TABLE}({COLNAMES}) VALUES({VALUES})'
        self.database = database
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.stmt=''
        self.params=''
        try:
            self.conn=mysql.connector.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database)
            if self.conn.is_connected():
                print('Connected to MySQL database')
            else:
                print('be ga raft')
                assert('Be ga raft!!')
        except ProgrammingError as e :
            sexyError(e)


    def setParams(self,params='<!No!>'):
        if params=='<!No!>' or params=='' or params==None :
            self.params = ''
        elif isinstance(params, numbers.Number):
            self.params=(params,)
        elif  isinstance(params,str):
            self.params =(params,)
        elif isinstance(params,list):
            self.params=tuple(params)
        elif isinstance(params,dict):
            self.params=tuple(params.values())
        elif isinstance(params,tuple):
            self.params=params




    def setStmt(self,stmt=''):
        self.stmt=stmt



    def exec(self,stmt='',params='<!No!>',all=0):
        self.setstmt = stmt
        self.setParams(params)
        cursor = self.conn.cursor(prepared=True)
        if self.params=='<!NO!>':
            ret = cursor.execute(self.stmt)
            ret = cursor.fetchall()
            return ret
        elif len(self.params)==0:
            ret = cursor.execute(self.stmt)
            ret = cursor.fetchall()
        else:
            ret = cursor.execute(self.stmt, self.params)
            ret = cursor.fetchall()
        self.conn.commit()
        cursor.close()
        return ret

    def bezar(self,table,colnames,vals):
        self.setParams(vals)
        if isinstance(colnames, list):
            colnames=virgool(colnames)
            valPlaceHolders=berin(len(vals),',%s',v=0)[1:]
        else:
            colnames = colnames
            valPlaceHolders = '%s'
        self.stmt = self.insrtStmt.format(TABLE=table, COLNAMES=colnames, VALUES=valPlaceHolders)
        ret =self.exec(self.stmt,self.params)
        return ret


    def begir(self,table,colnames,condition='<!no!>'):

        if condition=='<!no!>':
            self.stmt=self.stmtSlctNoCndt.format(TABLE=table, COLNAMES=colnames)
            self.params=''
            ret = self.exec(self.stmt)
        else:
            self.stmt = self.stmtSlctCndt.format(TABLE=table, COLNAMES=colnames, CONDITION='%s')
            berin(3, 'ppp')
            print(condition)
            berin(3, 'ppp')
            self.setParams(condition)
            ret = self.exec(self.stmt, self.params)
        return ret