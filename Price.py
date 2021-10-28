from datetime import datetime
from noche import berin

class Price(object):
    def __init__(self,vaght=datetime.now(),value=0,refCurrency=1,src='admin',jens='dool'):
        self.vaght=vaght
        self.value=value
        self.refCurrency=refCurrency
        self.src=src
        self.jens=jens
        self.exact=exact
    def xChange(self,neCur):
        pass
        #get Xchange Rate of curRef to neCur
        #update the abslout price value and newCur Simulataneously
    def compare(self,p:Price):
        pass
        #compare the current price instance with passed var

    def setPrice(self,val):
        self.price=val
    def getPrice(self):
        return self.price


    def getDic(self):
        return vars(self)











