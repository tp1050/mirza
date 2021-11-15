####Text Processing ####
#####Convertors######
""" convert Dictionary Obj to Str d= input dictionary  separator : Defualt is : but could be set to anything. """


def dic2str(d,separator=':',lines=False):
    if lines:
        retTMP='{}{}'
        ret=''
        tmp='{} {} {}{}'
        for i, j in d.items():
          ret=retTMP.format(ret,tmp.format(str(i),separator,str(j),'\n'))
        return ret
    else:
        return str(d)
        #json.dumps(d)


