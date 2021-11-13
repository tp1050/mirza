import datetime
import sys
import numbers
from StaticsBase import *

### Math Helpers
def ffloat(f):
    return float(f.replace(',', ''))


def mySQLTypeGen(element):
    print(element)
    if isinstance(element, numbers.Number):
        return 'float'
    else:
        return 'VARCHAR(256)'
def mySQLTypedFormat(e):
    if isinstance(e, numbers.Number):
        return  e
    else:
        return '`{}`'.format(e)

"""
Random Text helper
"""


"""   t$ for timestamp"""
def berin(n=1,sign='-',indent=0,v=1):
    indented=berin(n,' ')
    if sign=='t$':
        sign=datetime.now()
    s=''
    for i in range(n):
        s=sign+s
    s=indented+s
    if v:
        print(s)
    return s

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

def embrace(content,boundBy,boundBy2='<!NO!>'):
    ret = '{boundByL}{content}{boundByR}'
    if boundBy2==unIn:
        boundByL, boundByR=braces(boundBy)
    else:
        boundByL, boundByR = boundBy,boundBy2
    ret = ret.format(boundByL=boundByL, boundByR=boundByR, content=content)
    return ret

def virgool(inList,quotation='',sym=',',boundBy=''):
    boundByL, boundByR = embrace(boundBy)
    ret=''
    for item in inList:
            ret='{ret}{sym}{quotation}{item}{quotation}'.format(ret=ret,sym=sym,quotation=quotation,item=item)
    ret='{boundByL}{ret}{boundByR}'.format(boundByL=boundByL,ret=ret[1:],boundByR=boundByR)
    return ret


def sexyError(e):
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
    return 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e