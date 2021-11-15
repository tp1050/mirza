import numbers
import mysql.connector
from mysql.connector import ProgrammingError
import sys
from Khadang import *
from DegJet import *
from StaticsBase import *


class AnbarBase(DegJet):
    def connected(self):
        try:
            self.conn = mysql.connector.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                                database=self.database)
            if self.conn.is_connected():
                print('Connected to MySQL database')
            else:
                print('be ga raft')
                assert ('Khiar: Connection Nashod')
        except ProgrammingError as e:
            sexyError(e)


    def __init__(self,host='192.168.5.17',user='c',password='22111357',port=3306,database='Moozmar'):
        super().__init__()
   
        self.database = database
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.stmt=''
        self.params=''
   


    def setParams(self,params=UNIN):
        if params==UNIN or params=='' or params==None :
            self.params =UNIN
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
        return self.params





    def setStmt(self,stmt=''):
        self.stmt=stmt
        return self.stmt



    def exec(self,stmt='',params=UNIN,all=0):
        self.setStmt( stmt)
        self.setParams(params)
        ret=''
        try:
            cursor = self.conn.cursor(prepared=True)
            if self.params==('<!NO!>',) or self.params=='<!NO!>':
                ret = cursor.execute(self.stmt)
                ret = cursor.fetchall()
            else:
                ret = cursor.execute(self.stmt, self.params)
                ret = cursor.fetchall()
            self.conn.commit()
            cursor.close()
        except Exception as e:
            sexyError(e)
        if (isinstance(ret,list)):
            if len(ret)==1:
                print
        return ret

    def bezar(self,table,colnames,vals):
        self.setParams(vals)
        if isinstance(colnames, list):
            colnames=virgool(colnames)
            valPlaceHolders=berin(len(vals),',%s',v=0)[1:]
        else:
            colnames = colnames
            valPlaceHolders = '%s'
        self.stmt = INSRTCNDTION.format(TABLE=table, COLNAMES=colnames, VALUES=valPlaceHolders)
        ret =self.exec(self.stmt,self.params)
        return ret


    def begir(self,table,colnames,conCol=UNIN,condition=UNIN,limit=1):
        
        if isinstance(colnames, list):
            colnames = virgool(colnames, sql=1)
        else:
            colnames = mySQLTypedFormat(colnames)
            
        if condition==UNIN:            
            self.stmt=stmtSlctNoCndtion.format(TABLE=table, COLNAMES=colnames)
            self.params=''
            ret = self.exec(self.stmt)
        else:
            self.stmt = stmtSlctCndtion.format(TABLE=table, COLNAMES=colnames, CONDITION='%s',CONCOL=conCol)
            self.setParams(condition)
            print(self.stmt)
            ret = self.exec(self.stmt, self.params)
        return ret