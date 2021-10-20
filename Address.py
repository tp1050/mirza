class Address(object):
    def __init__(self,host='localhost',user='doolsaz',password='22111357',database='021',port=3306,serverType='mySql'):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.port=port
        self.serverType=serverType

    def setUser(self,user):
        self.user=user
    def getUser(self):
        return self.user

    def setHost(self,user):
        self.user=user
    def getHost(self):
        return self.user

    def setDatabase(self, user):
        self.user = user
    def getDatabase(self):
        return self.user

    def setPort(self,user):
        self.user=user
    def getPort(self):
        return self.user

    def setType(self,serverType):
        self.serverType = serverType
    def getType(self):
        return self.serverType

    def getLocation(self):
        tmp=(self.host,self.user,self.password)
        return tmp

