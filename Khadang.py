import datetime
import sys
import numbers

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
    if sign=='t$':
        sign=datetime.now()
    s=''
    for i in range(n):
        s=sign+s
    if v:
        print(s)
    return s

###########
def embrace(content,boundBy,boundBy2=boundBy):
    if boundBy==boundBy2:
        boundByL, boundByr=embrace
        ret='{}'
def embrace(boundBy):
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

    return boundByL,boundByR




def virgool(inList,quotation='',sym=',',boundBy=''):
    boundByL,boundByR=embrace(boundBy)
    ret=''
    for item in inList:
        ret=ret+'{sym}'.format(sym=sym)+'{quotation}{item}{quotation}'.format(quotation=quotation,item=item)
    ret='{boundByL}{ret}{boundByR}'.format(boundByL=boundByL,ret=ret[1:],boundByR=boundByR)
    return ret


def sexyError(e):
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
    return 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e