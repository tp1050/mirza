import datetime
import sys
import numbers
import socket
from StaticsBase import *

def getIpByHost(address):
    ip=UNIN
    try:
        ip=socket.gethostbyname(host)
    except Exception as e:
        prrint(e)
    return ip
def isLive(address):
      return getIpByHost()==True
   

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False
    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True


def isValidHostStr(hostStr):
        if is_valid_ipv4_address(hostStr):return True
        if is_valid_ipv6_address(hostStr):return True
        return False

### Math Helpers
def ffloat(f):
    return float(f.replace(',', ''))


def mySQLTypeGen(element):
    # print(element)
    if isinstance(element, numbers.Number):
        return 'float'
    else:
        return 'VARCHAR(256)'

def mySQLTypedFormat(e):
    if isinstance(e, numbers.Number):
        return  e
    elif e=='*':
        return '{}'.format('*')
    else:
        return '`{}`'.format(e)

"""
Random Text helper
"""


"""   t$ for timestamp"""
def berin(n=1,sign='-',indent=0,v=1):
    indented=''
    if indent>0:
        indented = berin(n=indent, sign=' ', indent=0, v=0)
    else:
        if sign=='t$':
            sign=datetime.datetime.now()
        ret= ''
        for i in range(n):
            ret= '{} {}'.format(sign , ret)
        ret= '{}{}'.format(indented, ret)
        if v:
            print(ret)
    return ret

###########

def braces(boundBy):
    boundByL=''
    boundByR=''
    if not boundBy == '':
        if boundBy == '(' or boundBy == ')':
            boundByL = '('
            boundByR = ')'
        elif boundBy == '{' or boundBy == '}':
            boundByL = '{'
            boundByR = '}'
        elif boundBy == '{' or boundBy == '}':
            boundByL = '{'
            boundByR = '}'
        elif boundBy == '<' or boundBy == '>':
            boundByL = '<'
            boundByR = '>'
        elif boundBy == '[' or boundBy == ']':
            boundByL = '['
            boundByR = ']'
        else:
            boundByL=boundBy
            boundByR=boundBy

    return boundByL,boundByR

def embrace(content,boundBy,boundBy2=UNIN):
    ret = '{boundByL}{content}{boundByR}'
    if boundBy2==unIn:
        boundByL, boundByR=braces(boundBy)
    else:
        boundByL, boundByR = boundBy,boundBy2
    ret = ret.format(boundByL=boundByL, boundByR=boundByR, content=content)
    return ret

def virgool(inList,quotation='',sym=',',boundBy='',sql=0):
    inlist2=[]
    if sql==1:
        for i in inList:
            inlist2.append(mySQLTypedFormat(i))
    inList=inlist2
    boundByL, boundByR = braces(boundBy)
    ret=''
    for item in inList:
            ret='{ret}{sym}{quotation}{item}{quotation}'.format(ret=ret,sym=sym,quotation=quotation,item=item)
    ret='{boundByL}{ret}{boundByR}'.format(boundByL=boundByL,ret=ret[1:],boundByR=boundByR)
    return ret


def sexyError(e):
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
    return 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e