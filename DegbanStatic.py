# """ localhost """
# # defHost="192.168.5.17"
# # defUser='doolsaz'
# # defPassword='22111357'
# # defDatabase='ks'
# """ C server """
# # defHost='84.241.63.0' # database error
# # defUser='aren'       # user and pass wrong: ProgrammingError
# # defPassword='karen'
# # defDatabase='ks'      # nothing till further notice !
#
# """ D server """
# defHost='localhost' # database error
# defUser='karen'       # user and pass wrong: ProgrammingError
# defPassword='Karen22111357*'
# defDatabase='ISP'      # nothing till further notice !
from Address import *
from anbar import *

base0LAN=Address(host='192.168.2.10',user='c',database='Moozmar')

class DegJet(object):

    def __init__(self,conn='No'):
        self.test='test2'
        self.conn=conn

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
            s = '{} : {} '.format(str(k) ,dic[k])+ sep + s
        return s
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
        bezar()
        # pp=berin(sign=',{}',n=len(dic.keys()))[1:]
        # print(pp)
        # i=0
        # for k in dic:
        #     berin(i,'+')
        #     print(dic[k])
        #     pp=pp.format()
        #     print(pp)
        #     i=i+1
        # # stmt=self.begoo(sep=',')
        # # bezar()
        print(s)