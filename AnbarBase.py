import mysql.connector
from mysql.connector import ProgrammingError
import sys
# import MySQLdb
from Khadang import *
from DegJet import *


class AnbarBase(DegJet):
    stmtSlctCndt='select %s from %s where %s=%s;'
    stmtSlct = 'select %s from %s;'
    insrtStmt=' insert into %s(<%$tmtCol%>) values(<%$tmtVals%>)'
    
    def __init__(self,host='192.168.5.17',user='c',password='22111357',port=3306,database='Moozmar'):
        super().__init__()
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
                print('be ga raft')
                assert('Be ga raft!!')
        except ProgrammingError as e :
            sexyError(e)
            
            

    # def mySQLize(s):
    #     return   MySQLdb.escape_string(s)

    def exec(self,stmt,all=0):
        mc = self.conn.cursor(prepared=True)
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
    
    
    
    def execPS(self,stmt,tuplee,all=1):
            mc = self.conn.cursor(buffered=True)
            recs="   "
        # try:
            mc.execute("""select %s from %s;""",('id','test',))
            print(34343)

            # self.conn.commit()
            print(3423423)
            if all==0:
                recs=mc.fetchone()
                return recs
            elif all==1:
                recs=mc.fetchall()
                return recs
            self.conn.commit()
        # except Exception as e:
        #     # print(mc.description())
        #     sexyError(e)
        #     mc.close()
            return recs


    def begir(self,tbl,col,condtion='',stmt=''):
        if condtion:
            stmt="""select %s from %s where {}="{}";""".format(col,tbl,col,condtion)
        else:
            stmt = 'select {} from {};'.format(col,tbl,col)
        ret=self.exec(stmt=stmt)
        return ret
    def begirPS(self,tbl,col,condtion=''):
        stmt=''
        if condtion:
            stmt = ("""select %s from %s where %s=%s;""",(col, tbl, col, condtion,))
            return stmt
        else:
            stmt = """select id from test; """,(col, tbl,)
            return stmt
        return -1
    
        
        
        
        
        
    def bezar(self,tbl,col,val):
        stmt='insert into {}({}) values({});'.format(tbl,col,val)
        print(stmt)
        return self.exec(stmt,all=9)



