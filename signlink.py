from netnoche import getHTML
import json
from bs4 import BeautifulSoup as bs
import requests

def getcPrice():
    priceInfoDict={}
    a=getHTML("https://api.accessban.com/v1/widget").splitlines()
    jjj=[]
    for aaa in aa:

        if 'var tgju' in aaa:
            # print(aaa)
            ggg=aaa.encode('latin1', 'backslashreplace').decode('unicode-escape').replace("var tgju_data = ","")
            ggg=ggg[:-1]
            # print(ggg)
            jjj=json.loads(ggg)

            # print (jjj)
        else:
            pass


    for key in jjj:
        jaj=jjj[key]
        price=jaj['p']

        print(jaj)
        # esm=jaj['']
        print(key, '  ', price)

def getPrice1():
    priceD={}
    content=getHTML("https://api.accessban.com/v1/widget")
    content1=content.splitlines()
    for i in content1:
        if 'var tggju' in i:
            ggg=i.encode('latin1','backslashreplace').decode('unicode-escape').replace('var tgju_data = ',"")
            ggg = ggg[:-1]
            contentList=json.loads(ggg)
        else:
            print('problem encountered')
            pass


    for key in contentList:
        keyItem=contentList[key]
        price=keyItem['p']
        title=keyItem['title']
        priceD['jens'] =title
        priceD['price']=price
    return priceD
td=[]
a=[]
# page=requests.get("https://www.xe.com/symbols.php")
page=getHTML("https://www.xe.com/symbols.php")
soup=bs(page,'html.parser')
for link in soup.find_all('img'):
    a=soup.find(class_='cSmbl_imgCol')
    td.append(link)
    td.append(a)

print(td)
print(a)