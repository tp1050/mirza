from Khadang import mySQLTypeGen,mySQLTypedFormat
from StaticsBase import unIn

# import MySQLdb
class DegJet(object):

    def __init__(self,conn=unIn,id=0):
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
            ret = ',{key}:{value}{sep}{ret}'.format(key=str(k) ,value=dic[k],sep=sep,ret=ret)
        return ret[1:]
    
    
    def sabt(self):
        tbl=self.name()
        dic=self.getDic()
        col= ''
        for k in dic:
            if k=='conn':
                continue
            col= col + ',' + '`{}`'.format(k)
        col= col[1:]
        val= ''
        for k in dic:
            if k == 'conn':
                continue
            val = val + ',' + '{}'.format(mySQLTypedFormat(dic[k]))
        val = val[1:]
        return {'tbl':self.name(), 'col':col, 'val':val}
    
    
    def makeDbTbl(self):
        dic=self.getDic()
        s=''
        for key in dic:
            s=s+',`{}` {}'.format(key,mySQLTypeGen(dic[key]))
        stmt='CREATE TABLE {}({});'.format(self.name(),s[1:])
        return stmt


    def str(self):
        return self.begoo()
    def __str__(self):
        return self.begoo()