from datetime import datetime
from Khadang import berin
from anbar import *
from DegbanStatic import *

class Price(DegJet):
    def __init__(self,vaght=datetime.now(),value=0,refCurrency='fx_irr',src='admin',jens='dool',refCurID=49,conn='no',exact=1,validUntill='09/09/25 09:09:09',jensID=0):
        self.vaght=vaght
        self.value=value
        self.refCurrency=refCurrency
        self.src=src
        self.jens=jens
        self.exact=exact
        self.conn = conn
        self.discountRate = 0
        self.validUntil = datetime.strptime(validUntill, '%d/%m/%y %H:%M:%S')
        if self.conn == 'NO':
            conn = getAnbar(base0LAN)
        self.jensID = jensID
        # if jensID == 0:
        #     self.jensID = getSymID(self.jens, conn)

    def berooze(self):
        return datetime.now()<self.validUntil

    def discount(self,discountRate=0):
        if discountRate==0:
            pass
        else:
            self.discountRate=discountRate
        self.value=+self.value-(self.value*self.discountRate)


    def getXchangeRate(self,cur1,cur2,vaght=datetime.now(),dirty=1,timeHedge=1,conn='No'):
        """
        Calculate the xChange Rate between two currencies. the relation is non transitive
        """
        ##{$HOMEWORK$}
        pass
    
    
    def xChange(self,newCur):
        """
        #{$HOMEWORK$}
        """
        newVal=self.value*getXchangeRate(self.refCurrency,newCur)
        self.refCurrency=newCur
        self.refCurID=getSymID(newCur)
        self.value=newVal
        #get Xchange Rate of curRef to neCur
        #update the abslout price value and newCur Simulataneously
        # {$HOMEWORK$}

    def compare(self,otherPrice):
        if self.refCurID==otherPrice.refCurID:
           if self.value>otherPrice.value:
               return 'Bigger'
           else:
               return 'Smaller'
        else:
            newMe=self.xChange('fx_irr')
            otherPrrice=otherPrice.xChange('fx_irr')
            return newMe.compare(otherPrice)

 
  
    def begoo(self):
        return (
            "{} claims: {} is sold  at {} {} at {}".format(self.src, self.jens, self.value,self.refCurrency, self.vaght))
########################


    def setPrice(self,val):
        self.price=val
    def getPrice(self):
        return self.price
    def setSrc(self,val):
        self.src=val
    def getSrc(self):
        return self.src







