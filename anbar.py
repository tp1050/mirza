from AnbarBase import AnbarBase
from Address import Address
from DegbanStatic import *


class Anbar(AnbarBase):
    def __init__(self,loc='No'):
        self.conn = ''
        if loc=='No':
            loc=base0LAN
        super().__init__(**loc.getLocation())

    def getDicID(self,org):
        res=-1
        stmt = 'select ID,eq from Moozmar.Dictionary where original="{}";'
        res=self.exec(stmt.format(org))
        if res is not None:
            res=res
        else:
            self.exec('insert into Moozmar.Dictionary(original) values("{}");'.format(org))
            res = self.getDicID(org)
        return res

    def getSymID(self, dicEq):
        stmt = 'select ID from Moozmar.Deg2Sym where sym="{}";'.format(dicEq)
        res = self.exec(stmt.format(dicEq))
        if res is not None:
            return res[0]
        return -1
    def sabt(self):
        a=super().sabt()
        self.bezar(**a)
        return a
    def makeDbTbl(self):
        self.exec(stmt=super().makeDbTbl(),all=9)






# import mysql.connector
# from mysql.connector import Error
# import sys
# from Address import *
# from noche import berin,sexyError

# def getAnbar(loc='No',secure=0):
#     if loc=='N0':
#         loc=Address()
#     if secure:
#         return False
#     l=loc.getLocation()
#     # print(l)
#     try:
#         conn = mysql.connector.connect(**l)
#         # berin(1,'%')
#         if conn.is_connected():
#             print('Connected to MySQL database')
#             return conn
#         else:
#             return None
#     except Error as e:
#         sexyError(e)
# def exec(stmt,conn='NO'):
#     passed=1
#     if conn=='NO':
#         conn = getAnbar()
#         passed = 0
#     mc = conn.cursor(buffered=True)
#     recs="   "
#     try:
#         mc.execute(stmt)
#         conn.commit()
#         recs=mc.fetchone()
#     except Exception as e:
#         sexyError(e)
#     mc.close()
#     if not passed:
#         conn.close()
#     return recs
#
#
#

#
#
#
#
# #
# # def getCurID(cur)
# """
# jason{
#
# 'Tabanle':''
# 'cols':{colname:value}
# }
# """
#
# ###
# #Bama Anbar Tools
#
# # def putBamaGahi(ins):
# #     pass
# #     rose:{
# #  # :'AutoDealer'
# #   'بدنه' :'BodyWork',
# #  # :
# # 'داخل' :'ColorIn',
# #  # :
# # 'رنگ':'ColorOut',
# #  'گیربکس': 'GearBox',
# #  # 'Mahaleh'
# #  # 'MashinSazi'
# #  'كاركرد': 'Milage ',
# #  # 'Model '         :
# # 'سوخت': 'Sookht'          :
# #  # 'Tel'             :
# #  'توضیج':'desc'
# #      }
# #  #    for keys in in:
# # def p(n):
# #     ret='%s'
# #     n=n-1
# #     while n>0:
# #         ret=ret+',%s'
# #     return 'values('+ret+')'
# # def pc(a):
# #     ret=a.pop()
# #     while( len(a)>0):
# #         ret=ret+','+a.pop()
# #     return '('+ret+')'
# #
# # def bezar(js):
# #     stmt='insert into {table} ({c}) values({v})'
# #     stmt=stmt.format(table=js['tabale'])
# #     print(stmt)
# #
# #
# # js2={}
# # cv={}
# # cv['url']='https://divar.ir/test/test'
# # js2['tabale']='Moozmar.jobs'
# # js2['cols']=cv
# # bezar(js2)
