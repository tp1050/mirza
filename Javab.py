class Javab(object):
    def __init__(self, ret='', error='200'):
        self.ret = ret
        self.error = error

    # eCodery={
    #     '001': 'Access denied ',
    #     '002': 'Unknown MySQL server host',
    #     '003': 'No database selected',
    #     '100': 'success'
    #     }
    def setError(e):
        self.error =e
    def setJavab(j):
        self.ret=j
    def getJavab():
        return self.ret
    def getError():
        return self.error

    def str(self):
        tmp='{} \n {}'.format(self.ret,self.error)
        return tmp
    def isMosbat(self):
        if self.error=='100':
            return True
        return False
    def save(self):
        save(str())

