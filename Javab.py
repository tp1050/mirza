class Javab(object):
    ret=''
    error='200'
    eCodery={
        '001': 'Access denied ',
        '002': 'Unknown MySQL server host',
        # when you do not specify a dbName and give the exec() the sql
        '003': 'No database selected',
        '100': 'success'
        }

    def Javab(self,r,e):
        error=e
        ret=r

    # private javab=''
    # private error=''k
    def setError(e):
        error =e
        def setJavab(j):
        ret=j
    def getJavab():
        return ret
    def getError():
        return error
    def str(self):
        tmp='{} \n {}'.format(ret,error)
        return tmp
    def isMosbat(self):
        if error=='100':
            return True
        return False
    def save(self):
        save(str())

