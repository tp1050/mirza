from DegJet import *
class UA(DegJet):
    def __init__(self,country='iran',city='tehran',county='vanak',district=0,street='vanak',postCode=0,vahed=0,zang=0,tozihat=''):
        super().__init__()
        self.country=country
        self.city=city
        self.county=country
        self.district=district
        self.street=street
        self.postCode=postCode
        self.vahed=vahed
        self.zang=zang
        self.tozihat=tozihat

    def getPrice(self):
        return self.pricePerSQM2()
    def getPMI(self):
        return 'PMI'
    def getTrafficIndex(self):
        return 'TF'
    def getAI(self):
        return 'AI'
    def connectivityI(self):
        return 'CI'
    def isEdari(self):
        return false
    def isTejari(self):
        return True
    def isMaskoni(self):
        return True
    def sanad(self):
        return true