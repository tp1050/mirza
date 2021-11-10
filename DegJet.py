from Khadang import mySQLTypeGen
import MySQLdb
class DegJet(object):

    def __init__(self,conn='No',id=0):
        self.id=id
        self.test='test2'
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
        s=''
        for k in dic:
            s=s+','+'{}'.format(k)
        s=s[1:]
        p=''
        for k in dic:
            p = p + ',' + '{}'.format(dic[k])
        p = p[1:]
        print(p)
        return (self.name,s,p,self.conn)
    def mkDBtBL(self):
        dic=self.getDic()
        s=''
        for key in dic:
            
            s=s+',{} {}'.format(key,mySQLTypeGen(key))

        print (s)
        stmt='create table {}({});'.format(self.name(),s[1:])
        return stmt