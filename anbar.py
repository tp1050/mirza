
#comment
import mysql.connector
from mysql.connector import Error
import sys

class Javab(Object):
    eCodery={
        'eCode1':001
        'ecode2':002
        'ecode3':003
        }
    def Javab(self,j,e):
        error=# -*- coding: utf-8 -*-
        javab=j
        
    private javab=''
    private error=''
    def setError(e):
        error =e
    def setJavab(j):
        javab=j
    def getJavab():
        return javab
    def getError():
        return Error







#Block access to internal Variables
defHost="192.168.5.17"
defUser='doolsaz'
defPassword='22111357'

#Option for secure connection
#Option for X-SQL sys
#ablity to connect via proxy
#active mysql discovery
def getAnbar(host=defHost,user=defUser,password=defPassword,secure=0):
    if secure:
        pass
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect( host=defHost,
                                        user=defUser,
                                        password=defPassword):
        if conn.is_connected():
            print('Connected to MySQL database')
            # conn.escape_string()
            return conn

    except Error as e:
        print(e)



"""
Execute any stmt
#Verobse on off
"""

def exec(stmt):
    j=Javab()
    #print('%s'%stmt)
    #code will shit itself if conn is null
    conn = getAnbar()
    mc = conn.cursor(buffered=True)
    recs=""
    try:
        mc.execute(stmt)
        conn.commit()
        recs=mc.fetchall()
        print(recs)
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        j.error='Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e
            #print(agahi)
    mc.close()
    conn.close()
    j.javab=str(recs)
    return j

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
