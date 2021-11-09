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

base0LAN=Address(host='192.168.2.10',user='c',database='Moozmar')

class Degjet(object):
    def begoo(self):
        ret=''
        for a in vars(self):
            s=str(a)+' '+s
        return s
    def sabt(self):
        pass