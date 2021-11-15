import Khadang
from DegJet import *
from Khadang import isValidHostStr
import numbers
class NewAddress(DegJet):
    def __init__(self,host='localhost',user='doolsaz',password='22111357',database='021',port=3306,serverType='mySql'):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.port=port
        self.reachble=0
        # self.serverType=serverType

    @property
    def host(self):
        return self._host
    @host.setter
    def host(self, host,chkLive=0):
        if isValidHostStr(host):
            self._host = host
        else:
            raise Exception('Khiar')
        if chkLive:
            print(Khadang.getIpByHost(host))
            self.reachble=Khadang.isLive(host)
            print(self.reachble)




    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, user):
        self._user = user

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,password):
        self._password = password

    @property
    def database(self):
        return self._database
    @database.setter
    def database(self,database):
        self._database = database
        
    @property
    def port(self):
        return self._port
    @port.setter
    def port(self,port):
        if isinstance(port,numbers.Number):
            self._port = port
        else:
            raise Exception('Khair!')    

    def getLocation(self):
        temp={}
        temp['host']=self.host
        temp['user']=self.user
        temp['password']=self.password
        temp['port']=self.port
        temp['database']=self.database
        res=temp
        return res

