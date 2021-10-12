#comment
import mysql.connector
from mysql.connector import Error
import sys
import subprocess

class Javab(object):
    eCodery={
        '001': 'Access denied ',
        '002': 'Unknown MySQL server host',
        # when you do not specify a dbName and give the exec() the sql
        '003': 'No database selected',
        }

    def Javab(self,j,e):
        error=e
        javab=j

    # private javab=''
    # private error=''
    def setError(e):
        error =e

    def setJavab(j):
        javab=j
    def getJavab():
        return javab
    def getError():
        return Error


#Block access to internal Variables

""" localhost """
# defHost="192.168.5.17"
# defUser='doolsaz'
# defPassword='22111357'
# defDatabase='ks'
""" C server """
# defHost='84.241.63.0' # database error
# defUser='aren'       # user and pass wrong: ProgrammingError
# defPassword='karen'
# defDatabase='ks'      # nothing till further notice !
""" D server """
defHost='localhost' # database error
defUser='karen'       # user and pass wrong: ProgrammingError
defPassword='Karen22111357*'
defDatabase='ISP'      # nothing till further notice !
#Option for secure connection
#Option for X-SQL sys
#ablity to connect via proxy
#active mysql discovery

"""a function for make mysql server running """

def sysMysqlCmd():
    pass

def getAnbarReconn(Host, User , Password ,DbName,secure=0):
    if secure:
        pass

    try:
        conn=None
        conn=mysql.connector.connect(host=Host,
                                     user=User,
                                     password=Password,
                                     database=DbName,
                                     )
        if conn.is_connected():
            print('Reconnected successfully ')
        return conn
    except mysql.connector.errors.DatabaseError as e:
        #ask user input for  make mysql up and running by executing system cmds in script
        usrin=input("The MYSQL-server you are accessing is down you wish to set it up again? y\n to continue \nBe aware you need clearance ! ")
        # find a way to execute  with out asking for root password
        #this is working for know
        if usrin=='y':
            prc=subprocess.run(['sudo','service','mysql','status'],capture_output=True)
            if 'Active: inactive (dead)' in str(prc):
                print('Confirmed that MYSQL server was down setting up ... ')
        # to be  continued...


    except Error as e:
        print(e)

def getAnbar(host=defHost,user=defUser,password=defPassword,database=defDatabase,secure=0):
    if secure:
        pass
    #resp=javab()
    """ Connect to MySQL database """
    try:
        conn = None
        conn = mysql.connector.connect( host=defHost,
                                        user=defUser,
                                        password=defPassword,
                                        database=defDatabase,
                                    )
        # connType: mysql.connector.connection_cext.CMySQLConnection
        if conn.is_connected() :
            print('Connected to MySQL database')
        return conn

    except mysql.connector.errors.ProgrammingError as PrgmErr:
        #resp.error='Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(PrgmErr).__name__, PrgmErr
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(PrgmErr).__name__, PrgmErr)
        # if user or pass  is wrong , >>>ussing pass is set to yes and not freeze
        print('user or pass is wrong ,check them and try to reconnect :')
        getAnbarReconn(Host=input('enter host: '),User=input('enter user: '),Password=input('enter pass: '),DbName=input('enter dbname: '))


    except mysql.connector.errors.DatabaseError as e:
        #resp.error='Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        print('2 possible situation : \n1-Wrong MYSQL address \n2-MYSQL serer is DOWN\nif its Sit1 is the case then : \n Reconnecting :')
        getAnbarReconn(Host=input('Enter the host CAREFULLY !: '),User=defUser , Password=defPassword,DbName=defDatabase)
        # except mysql.connector.errors.DatabaseError as e:
        #     print("The MYSQL-server you are accessing is down you wish to set it up again? \nBe aware you need clearance ! ")
        # ip addr for host is wrong
        # handle function
                # <class 'mysql.connector.errors.DatabaseError'>
        #2003 (HY000): Can't connect to MySQL server on '184.241.63.0:3306' (110)

        print(e)
    except Error as e :
        #resp.error='Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        print(type(e))

#getAnbar()
# mysql.connector.errors.DatabaseError


"""
Execute any stmt
#Verobse on off
"""
        # print('------------------------')
        # print(type(e))
def exec(stmt):
    resp=Javab()
    #print('%s'%stmt)
    #code will shit itself if conn is null
    try:
        conn = getAnbar()
        # if getAnbar doesnt function line below (line93) is the breakpoint
        # and you cannot write an if stmt /python ignore anything kt has done with the conn obj !!!
        mc = conn.cursor(buffered=True)

        recs=""
        # code will break if no db is selected
        mc.execute(stmt)
        conn.commit()
        recs=mc.fetchall()
        print(recs)
        mc.close()
        conn.close()
        resp.javab=str(recs)

    except mysql.connector.errors.ProgrammingError as PrgmErr:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(PrgmErr).__name__, PrgmErr)
        resp.error='Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(PrgmErr).__name__, PrgmErr
        print(resp.error)
        # retry connecting
        """ a function that recnnect to db via mysql and try some other ways till 3 times """

    except AttributeError as atrErr:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(atrErr).__name__, atrErr)
        resp.error='Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(atrErr).__name__, atrErr

    except Exception as e:
        print(type(e))

        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        resp.error='Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e

            #print(agahi)

    return resp

def begir():
    pass

sqlstmt="""select * from ip2location_country_information  limit 10"""

exec(sqlstmt)

#print(exec('select * from ip2location_country_information'))
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
