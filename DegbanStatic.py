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
            s=k+','+s
        pp=berin(sign=',{}',n=slen(dic))[1:]
        for k in dic:
            pp=pp.format(dic[k])
        # stmt=self.begoo(sep=',')
        # bezar()
        print(s,pp)