import platform
import IP2Proxy
from noche import dic2str
import re
import psutil
import platform
# for gpu 
import GPUtil
from tabulate import tabulate
from datetime import datetime




"""
Resiliant/reliable
IP check
arguments
standPoint= LOCAL|GLOBAL|ALL
Local= local IP
Global= Global IP IP
Default=ALL

"""
def myIP(session=requests.session()):
    """
    Stuborn function to extract callerIP for a passed sesssion.
    """
    provider =[ 'http://farbodfarjadi.rf.gd/',
                'https://www.cloudflare.com/cdn-cgi/trace',
                'https://idenrrt.me/',
                'http://icanhazip.com',
                'http://httpbin.org/ip',
                'http://checkip.amazonaws.com/']
    ret=[]

    for p in provider:
        res="2"
        try:

            # res = session.get(p).text
            print('trying : ' +p)
            res=getHTML(p)
            s=re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',res)
            ret.append(s)
        except Exception as e:
            ret.append(e.args)
    return ret




"""
REturns True if the IP provided is VPN/PROXY PROVIDER OR TOR exit node
"""


db = IP2Proxy.IP2Proxy()
# open IP2Proxy BIN database for proxy lookup
db.open("IP2PROXY-LITE-PX10.BIN")

def isproxy(proxyip):

    # get versioning information
    versionDict = {
            'Module Version'  : db.get_module_version() ,
            'Package Version'  : db.get_package_version() ,
            'Database Version'  : db.get_database_version(),
        }

    # single function to get all proxy data returned in array
    # this returns a dict 
    record = db.get_all(proxyip)
    userinput = input('if you want the info to be shown enter p otherwise enter c :')
    if userinput == 'p' :

        print ('Is Proxy: ' + str(record['is_proxy']))
        print ('Proxy Type: ' + record['proxy_type'])
        print ('Country Code: ' + record['country_short'])
        print ('Country Name: ' + record['country_long'])
        print ('Region Name: ' + record['region'])
        print ('City Name: ' + record['city'])
        print ('ISP: ' + record['isp'])
        print ('Domain: ' + record['domain'])
        print ('Usage Type: ' + record['usage_type'])
        print ('ASN: ' + record['asn'])
        print ('AS Name: ' + record['as_name'])
        print ('Last Seen: ' + record['last_seen'])
        print ('Threat: ' + record['threat'])
        print ('Provider: ' + record['provider'])
        print (versionDict['Module Version'])
        print (versionDict['Package Version'])
        print (versionDict['Database Version'])
    else:

        # close IP2Proxy BIN database
        db.close()

    # Web Service
    ws = IP2Proxy.IP2ProxyWebService("demo","PX11",True)
    rec = ws.lookup("89.208.35.79")
    print ("\n")
    print ("Credit Remaining: {}\n".format(ws.getcredit()))


"""
Method provides system info

Takes as argument

BioType:   Soft|Hard|Full 
software bio
hardware bio
defualt set to Hard


"""
def getSize(bytes, suffix='B'):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor 

def whoAmI2():
	info = {}
	info["platform details"]  = platform.platform()
	info["system name"]= platform.system()
	info["processor name"]  = platform.processor()
	info["architectural detail"] = platform.architecture()
	return dic2str(info)



"""
Retruns the Geo Data using current IP
Arguemnts:

ip=current ip defualt --> finds the IP itself

details=  Full|COUNTRY|CITY Default full 
"""
def whereAmI(ip=myIP(),details="full"):
	return ""


"""
returns a summery snapshot of system
such as memory usage
cpu usage etc
"""
def howAmI():
    pass

"""
A method to identify the service provicder and type of service
e.g 3g serrvice by Tmobile or Verozion 
ISP 

"""

def getProvider(ip=myIP()):
    p=""
    return p

