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
        self.test='test'
        self.conn=conn

    def getDic(self):
        return vars(self)
    def begoo(self,sep=' '):
        ret = ''
        for a in getDic():
            s = str(a) + sep + s
        return s
    def sabt(self):
        dic=self.getDic()
        s=''
        for k in dic:
            s=s+','+k
        s=s[1:]
        print(s)
        pp=berin(sign=',{}',n=len(dic.keys()))[1:]
        print(pp)
        i=0
        for k in dic:
            berin(i,'+')
            print(dic[k])
            pp=pp.format((k,dic[k]))
            print(pp)
            i=i+1
        # stmt=self.begoo(sep=',')
        # bezar()
        print(s,pp)