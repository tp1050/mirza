import mysql.connector
import csv

# the user input data goes here:
filepath ='ir.csv'
#the tableName should follow this pattern : dbName.tableName
tableName='fortest.boz'
dbName= 'fortest'

def mysqlConnector():

    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(
                                        host='localhost',
                                        user='karen',
                                        password='Karen22111357*',

                                        )
        if conn.is_connected():
            print('Connected to MySQL database')
            # conn.escape_string()
            return conn

    except Exception as e:
        print(e)

# an automated function with this output :
#'INSERT INTO ks.currencies (Country,CountryCode,Currency,Code) VALUES(%s,%s,%s,%s)'
def  autoSqlProducer():
    # INSERT INTO ISP.iranIsp (form , to , number , dateassigned , incName ) VALUES (%s,%s,%s,%s,%s)
    # cursor.execute(sql,(row[0],row[1],row[2],row[3]))

    with open('ir.csv','r+' ) as f:
        csvR=csv.reader(f)
        row1 =next(csvR)

    L=range(len(row1))
    # str for using in sql column specifier
    ks=''
    for i in L:
        ks = ks + row1[i] +","
    ks = "("+ ks[:-1] +")"

    # str for using in sql value specifier
    val =''
    for i in L:
        val=val +"%s,"
    val ="("+val[:-1]+")"

    sql =f"INSERT INTO {tableName} {ks} VALUES {val}"
    
    return sql

#        mc.execute(stmtInsertAgahi,(agahi['description'],agahi['price'],agahi['size'],agahi['location'],' '.join(agahi['phone']),j[0],agahi['sahebAD'],agahi['title'],agahi['city'],agahi['img']))
#    stmtInsertAgahi='INSERT INTO Moozmar.agahi(description,price,size,location,phone,url,sahebAgahi,title,city,img)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'


def insertion():

    with open(filepath,'r') as readObj:
        csvReader=csv.reader(readObj)
        # removing the headers : attention if you are using you must not remove the first row
        next(csvReader,None)
        for row in csvReader:
            sql=str(autoSqlProducer())
            # # print(row[0],row[1],row[2],row[3],row[4])
            # cursor.execute(sql,(row[0],row[1],row[2],row[3],row[4]))

    mydb.commit()

mysqlConnector()
mydb=mysqlConnector()
cursor=mydb.cursor()
insertion()
cursor.close()
