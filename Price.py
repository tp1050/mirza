from datetime import datetime
from noche import berin
from anbar import *
from DegbanStatic import *

class Price(DegJet):
    def __init__(self,vaght=datetime.now(),value=0,refCurrency='fx_irr',src='admin',jens='dool',refCurID=49,conn='no'):
        self.vaght=vaght
        self.value=value
        self.refCurrency=refCurrency
        self.src=src
        self.jens=jens
        self.exact=exact
        self.conn = conn
        if self.conn == 'NO':
            conn = getAnbar(base0LAN)
        self.jensID = jensID
        if jensID == 0:
            self.jensID = getSymID(self.jens, conn)
   
   
   
   
   
   
    def etXchangeRate(self,a,b):
        return 0.7
    
    
    
    
    
    def xChange(self,newCur):
        newVal=self.value*getXchangeRate(self.refCurrency,newCur)
        self.refCurrency=newCur
        self.refCurID=getSymID(newCur)
        self.value=newVal
        #get Xchange Rate of curRef to neCur
        #update the abslout price value and newCur Simulataneously
    def compare(self,p:Price):
        if self.refCurID==p.refCurID:
           if self.value>p.value:
               return 'Bigger'
           else:
               return 'Smaller'
        else:
            pass


  
    def begoo(self):
        return (
            "{} claims: {} is sold  at {} {} at {}".format(self.src, self.jens, self.value,
                        
                        
                        
                        
                        
                        
                                                                                     self.refCurrency, self.vaght))
########################


    def setPrice(self,val):
        self.price=val
    def getPrice(self):
        return self.price
    def setSrc(self,val):
        self.src=val
    def getSrc(self):
        return self.src







