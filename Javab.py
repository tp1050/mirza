# from noche import save as saveNoche
class Javab(object):
    def __init__(self, ret='   ', error='200'):
        self.ret = ret
        self.error = error
    def Javab(self, ret='   ', error='200'):
        self.ret = ret
        self.error = error
    def setError(self,e):
        self.error =e

    def setJavab(self,j):
        self.ret=j

    def getJavab(self):
        return self.ret

    def getError(self):
        return self.error

    def isMosbat(self):
        if self.error=='100':
            return True
        return False

    # def save(self):
    #     saveNoche(self.str())


    def str(self):
      tmp='{} \n {}'.format(self.ret,self.error)
      return tmp

    # eCodery={
    #     '001': 'Access denied ',
    #     '002': 'Unknown MySQL server host',
    #     '003': 'No database selected',
    #     '100': 'success'
    #     }