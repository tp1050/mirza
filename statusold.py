import platform
from noche import dic2str





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
def isProxy(ip):
	pass


"""
Method provides system info

Takes as argument

BioType:   Soft|Hard|Full 
software bio
hardware bio
defualt set to Hard


"""

def whoAmI():
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

