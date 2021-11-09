import mysql.connector
from mysql.connector import Error
import sys
from Address import *
from noche import berin,sexyError
import MySQLdb
def mySQLize(s):
    return   MySQLdb.escape_string(s)
def getAnbar(loc:Address=Address(),secure=0):
    if secure:
        return False
    # conn = None
    l=loc.getLocation()
    print(l)
    try:
        conn = mysql.connector.connect(**l)
        # berin(1,'%')
        if conn.is_connected():
            print('Connected to MySQL database')

            return conn

    except Error as e:
        sexyError(e)
def exec(stmt,conn='NO'):
    passed=1
    if conn=='NO':
        conn = getAnbar()
        passed = 0
    mc = conn.cursor(buffered=True)
    recs="   "
    try:
        mc.execute(stmt)
        conn.commit()
        recs=mc.fetchone()
    except Exception as e:
        sexyError(e)
    mc.close()
    if not passed:
        conn.close()
    return recs



def begir(tbl,col,cndtion,conn='NO'):
    if conn=='NO':
        conn = getAnbar()
    stmt='select {} from {} where {}="{}";'
    stmt2=stmt.format(col,tbl,col,cndtion)
    ret=exec(stmt2)
    return ret

def getDicID(org,conn='NO'):
    res=-1
    if conn=='NO':
        conn = getAnbar()
    stmt = 'select ID,eq from Moozmar.Dictionary where original="{}";'
    res=exec(stmt.format(org), conn)
    if res is not None:
        # print(res)
        res=res

    else:
        exec('insert into Moozmar.Dictionary(original) values("{}");'.format(org),conn)
        res=getDicID(org,conn)
    return res

def getSymID(dicEq,conn = 'NO'):
    if conn == 'NO':
        conn = getAnbar()
    stmt = 'select ID from Moozmar.Deg2Sym where sym="{}";'.format(dicEq)

    res = exec(stmt.format(dicEq), conn)
    if res is not None:
        return res[0]
    # print(res)
    return -1


#
# def getCurID(cur)
"""
jason{

'Tabanle':''
'cols':{colname:value}
}
"""

###
#Bama Anbar Tools

# def putBamaGahi(ins):
#     pass
#     rose:{
#  # :'AutoDealer'
#   'بدنه' :'BodyWork',
#  # :
# 'داخل' :'ColorIn',
#  # :
# 'رنگ':'ColorOut',
#  'گیربکس': 'GearBox',
#  # 'Mahaleh'
#  # 'MashinSazi'
#  'كاركرد': 'Milage ',
#  # 'Model '         :
# 'سوخت': 'Sookht'          :
#  # 'Tel'             :
#  'توضیج':'desc'
#      }
#  #    for keys in in:
# def p(n):
#     ret='%s'
#     n=n-1
#     while n>0:
#         ret=ret+',%s'
#     return 'values('+ret+')'
# def pc(a):
#     ret=a.pop()
#     while( len(a)>0):
#         ret=ret+','+a.pop()
#     return '('+ret+')'
#
# def bezar(js):
#     stmt='insert into {table} ({c}) values({v})'
#     stmt=stmt.format(table=js['tabale'])
#     print(stmt)
#
#
# js2={}
# cv={}
# cv['url']='https://divar.ir/test/test'
# js2['tabale']='Moozmar.jobs'
# js2['cols']=cv
# bezar(js2)
