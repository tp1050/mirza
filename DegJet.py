from Khadang import mySQLTypeGen
import MySQLdb
class DegJet(object):

    def __init__(self,conn='No',id=0):
        self.id=id
        self.conn=conn

    def name(self):
        return self.__class__.__name__
    def getDic(self):
        """
        REturns a dictionary containing the instance variables
        """
        return vars(self)

    def begoo(self,sep=' '):
        """
        Produces a String CURRENT*STATE of the instance
        """
        ret = ''
        dic=self.getDic()
        for k in dic:
            ret = ', {} : {} '.format(str(k) ,dic[k])+ sep + ret
        return ret[1:]
    
    
    def sabt(self):
        dic=self.getDic()
        columns= ''
        for k in dic:
            columns= columns + ',' + '`{}`'.format(k)
        columns= columns[1:]
        rows= ''
        for k in dic:
            rows = rows + ',' + '{}'.format(dic[k])
        rows = rows[1:]
        return self.name(), columns, rows
    
    
    def makeDbTbl(self):
        dic=self.getDic()
        s=''
        for key in dic:
            s=s+',`{}` {}'.format(key,mySQLTypeGen(dic[key]))
        stmt='CREATE TABLE {}({});'.format(self.name(),s[1:])
        return stmt