def p(n):
    ret='%s'
    n=n-1
    while n>0:
        ret=ret+',%s'
    return 'values('+ret+')'
def pc(a):
    ret=a.pop()
    while( len(a)>0):
        ret=ret+','+a.pop()
    return '('+ret+')'

def bezar(js):
    stmt='insert into {table} ({c}) values({v})'
    stmt=stmt.format(table=js['tabale'])
    print(stmt)


js2={}
cv={}
cv['url']='https://divar.ir/test/test'
js2['tabale']='Moozmar.jobs'
js2['cols']=cv
bezar(js2)
