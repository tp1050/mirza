class DegJet(object):

    def __init__(self,conn='No'):
        self.test='test2'
        self.conn=conn

    def getDic(self):
        """
        REturns a dictionary containing the instance variables
        """
        return vars(self)

    def begoo(self,sep=' '):
        """
        Produces a String CURRENT*STATE of the instance
        """
        ret = ''
        dic=self.getDic()
        for k in dic:
            ret = ', {} : {} '.format(str(k) ,dic[k])+ sep + ret
        return ret[1:]
    def sabt(self):
        dic=self.getDic()
        s=''
        for k in dic:
            s=s+','+'{}'.format(k)
        s=s[1:]
        p=''
        for k in dic:
            p = p + ',' + '{}'.format(dic[k])
        p = p[1:]
        print(p)
        # bezar()
        # pp=berin(sign=',{}',n=len(dic.keys()))[1:]
        # print(pp)
        # i=0
        # for k in dic:
        #     berin(i,'+')
        #     print(dic[k])
        #     pp=pp.format()
        #     print(pp)
        #     i=i+1
        # # stmt=self.begoo(sep=',')
        # # bezar()
        print(s)