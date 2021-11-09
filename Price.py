from datetime import datetime
from noche import berin
from anbar import *

class Price(object):
    def __init__(self,vaght=datetime.now(),value=0,refCurrency=1,src='admin',jens='dool',refCurID=0):
        self.vaght=vaght
        self.value=value
        self.refCurrency=refCurrency
        self.src=src
        self.jens=jens
        self.exact=exact
    def etXchangeRate(self,a,b):
        return 0.7
    def xChange(self,newCur):
        newVal=self.value*getXchangeRate(self.refCurrency,newCur)
        self.refCurrency=newCur
        self.refCurID=getSymID(newCur)
        self.value=newVal
        #get Xchange Rate of curRef to neCur
        #update the abslout price value and newCur Simulataneously
    # def compare(self,p:Price):
    #     pass
    #     #compare the current price instance with passed var

    def setPrice(self,val):
        self.price=val
    def getPrice(self):
        return self.price
    def setSrc(self,val):
        self.src=val
    def getSrc(self):
        return self.src
    def getDic(self):
        return vars(self)

    def begoo(self):
        return (
            "{} claims: {} is sold  at {} {} at {}".format(self.src, self.jens, self.value,
                                                                                     self.refCurrency, self.vaght))











