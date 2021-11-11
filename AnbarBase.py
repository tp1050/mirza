import mysql.connector
from mysql.connector import ProgrammingError
import sys
# import MySQLdb
from Khadang import *
from DegJet import *


class AnbarBase(DegJet):
    def __init__(self,host='192.168.5.17',user='c',password='22111357',port=3306,database='Moozmar'):
        super().__init__()
        self.stmtSlctCndt = 'SELECT {COLNAMES} from {TABLE} where {CONDITION};'
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


    def setParams(self,params=''):
        if isinstance(params,list):
            self.params=tuple(params)
        elif isinstance(params,dict):
            self.params=params.values()
        else:
            self.params=(params,)
        return self.params
    def setStmt(self,stmt=''):
        self.stmt=stmt



    def exec(self,stmt='',params='',all=0):
        if not stmt=='':
            self.stmt=stmt
            self.params = params
        cursor=self.conn.cursor(prepared=True)
        ret=cursor.execute(self.stmt,self.params)
        self.conn.commit()
        ret=cursor.fetchall()
        cursor.close()
        return ret

    def bezar(self,tbl,cols,vals):
        self.setParams(vals)
        if isinstance(cols, list):

            valPlaceHolders = ''
            for ccc in cols:
                valPlaceHolders = valPlaceHolders + ',{}'.format('%s')
            colnames=virgool(cols)
            valPlaceHolders = valPlaceHolders[1:]
            valPlaceHolders=berin(len(vals),',%s')[1:]


        else:
            colnames = cols

            valPlaceHolders = '%s'
        self.stmt = self.insrtStmt.format(TABLE=tbl, COLNAMES=colnames, VALUES=valPlaceHolders)
        ret =self.exec(self.stmt,self.params)
        return ret
    def begir(self,tbl,colnames,condition='<!no!>'):
        if condition=='<!no!>':
            self.stmt=self.stmtSlctNoCndt.format(TABLE=tbl,COLNAMES=colnames)
            self.params=''
        else:
            self.stmt = self.stmtSlctCndt.format(TABLE=tbl, COLNAMES=colnames,CONDITION=condition)
            self.params=(condition,)
        ret= exec(self.stmt,self.params)

