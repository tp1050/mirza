

### Math Helpers
def ffloat(f):
    return float(f.replace(',', ''))


"""
Random Text helper
"""


"""   t$ for timestamp"""
def berin(n=1,sign='-',indent=0):
    if sign=='t$':
        sign=datetime.now()
    s=''
    for i in range(n):
        s=sign+s
    print(s)
    return s

###########

def sexyError(e):
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
    return 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e