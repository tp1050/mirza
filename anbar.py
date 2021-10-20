
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
        berin(1,'%')
        if conn.is_connected():
            print('Connected to MySQL database')

            return conn

    except Error as e:
        print(e)



def exec(stmt):
    conn = getAnbar()
    mc = conn.cursor(buffered=True)
    recs=""
    try:
        mc.execute(stmt)
        conn.commit()
        recs=mc.fetchall()
        print(recs)
    except Exception as e:
        sexyError(e)
    mc.close()
    conn.close()
    recs=str(recs)
    return recs

def begir():
    pass


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
