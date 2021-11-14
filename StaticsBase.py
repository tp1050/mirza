



"""STATIC GLOBAL ENV"""
UNIN='<!NO!>'
FOREVER='00/00/00 00:00:00'


""" REGEXP"""
ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"



"""MYSQL STMS"""
stmtSlctCndtion= 'SELECT {COLNAMES} from {TABLE} where {CONCOL}={CONDITION};'
stmtSlctNoCndtion = 'select {COLNAMES} from {TABLE};'
INSRTCNDTION= 'INSERT INTO {TABLE}({COLNAMES}) VALUES({VALUES})'
