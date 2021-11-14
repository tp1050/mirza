from datetime import datetime
from Khadang import berin
from anbar import *
from DegbanStatic import *
from DegJet import *
from StaticsBase import *
class Price(DegJet):
    def __init__(self,value=0,refCurrency=UNIN,refCurID=0,jens=UNIN,jensID=0,src='admin',exact=1,vaght=datetime.now(),validUntill='09/09/25 09:09:09',historical=1,anbari=UNIN):
        super().__init__()
        self.exact = exact
        self.discountRate = 0
        self.historical = historical and True
    
        self.vaght = vaght
        self.validUntil = datetime.strptime(validUntill, '%d/%m/%y %H:%M:%S')

        self.src = src
        self.value = value
        
        self.jens = jens
        self.jensID = jensID

        self.refCurrency = refCurrency
        self.refCurID = refCurID
    
        if anbari==UNIN:
            self.anbari=Anbar(base0LAN)
        if self.jens==UNIN:
            self.jens=self.anbari.getJenByID(self.jensID)
        elif self.jensID<1:
            self.jensID=self.anbari.getSymID(self.jens)
        if self.refCurrency==UNIN:
            self.refCurrency=anbari.getJensById(self.refCurID)
        elif self.refCurID<1:
            self.anbari.getSymID(self.refCurrency)
            
    

    def berooze(self):
        if historical:
            return historical
        return datetime.now()<self.validUntil

    def discount(self,discountRate=0):
        if discountRate==0:
            pass
        else:
            self.discountRate=discountRate
        self.value=+self.value-(self.value*self.discountRate)
        return self.value


    def getXchangeRate(self,cur1,cur2,vaght=datetime.now(),dirty=1,timeHedge=1,conn='No'):
        """
        Calculate the xChange Rate between two currencies. the relation is non transitive
        """
        ##{$HOMEWORK$}
        return 0.7
    
    
    def xChange(self,newCur='fx_irr'):
        """
        #{$HOMEWORK$}
        """
        if self.refCurrency==newCur():
            return self.value

        newVal=self.value*getXchangeRate(self.refCurrency,newCur)
        self.refCurrency=newCur
        self.refCurID=anbari.getSymID(newCur)
        self.value=newVal
        #get Xchange Rate of curRef to neCur
        #update the abslout price value and newCur Simulataneously
        # {$HOMEWORK$}
        return this.value

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







