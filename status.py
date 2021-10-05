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
    # Web Service
    ws = IP2Proxy.IP2ProxyWebService("demo","PX11",True)
    rec = ws.lookup("89.208.35.79")

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
        print("\n")
        print("Credit Remaining: {}\n".format(ws.getcredit()))
    else:
        pass
        # close IP2Proxy BIN database
        db.close()
    return versionDict,record





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


def whoAmI():
    uname = platform.uname()
    sysInfoDict = {
        'System': uname.system,
        'Name': uname.node,
        'Release': uname.release,
        'Version': uname.version,
        'Machine': uname.machine,
        'Processor': uname.processor
    }

    # for cpu
    cpuFreq = psutil.cpu_freq()
    cpuInfoDict = {
        'physical cores': psutil.cpu_count(logical=False),
        'total cores': psutil.cpu_count(logical=True),
        'current frequency': cpuFreq.current,
        'max frequency': cpuFreq.max,
        'min frequency': cpuFreq.min,
        'Total CPU Usage': psutil.cpu_percent()
    }

    # CPU Usage Per Core
    coreList = []
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        # print(f"Core {i}: {percentage}%")
        coreList.append(i)
        coreList.append(percentage)

    # boot time apparently !
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)

    # getting RAM info
    sysMem = psutil.virtual_memory()

    # get the memory details
    sysMem = psutil.virtual_memory()

    # get the swap memory details (if exists)
    swap = psutil.swap_memory()

    # partition disk partitionning
    partitions = psutil.disk_partitions()
    partList = []
    diskIoList = []
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            print('this can be catched due to the disk that isnt ready')
            continue
        diskInfoDict = {
            'device': partition.device,
            'mountpoint': partition.mountpoint,
            'file system type': partition.fstype,
            'Total Size': getSize(partition_usage.total),
            'Used': getSize(partition_usage.used),
            'Free': getSize(partition_usage.free),
            'Percentage': f"  Percentage: {partition_usage.percent}%",
        }

        partList.append(diskInfoDict)

    diskIo = psutil.disk_io_counters()
    for disk in diskIo:
        try:
            diskIoDict = {
                'Total read': getSize(diskIo.read_bytes),
                'Total write': getSize(diskIo.write_bytes),
            }
        except Exception as e:
            print('oops accessing disk_io_counters hit a wall')

        diskIoList.append(diskIoDict)

    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                INETdict = {
                    'IP Address': address.address,
                    'Netmask': address.netmask,
                    'Broadcast IP': address.broadcast,
                }
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                PACKETdict = {
                    'MAC Address': address.address,
                    'Netmask': address.netmask,
                    'Broadcast MAC': address.broadcast,
                }
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    netIoDict = {
        'Total Bytes Sent': getSize(net_io.bytes_sent),
        'Total Bytes Received': getSize(net_io.bytes_recv),
    }

    userInp = input('if you want to see the info enter p otherwise enter c :')
    if userInp == 'p':
        # Cpu info
        print(f"Max Frequency: {cpuInfoDict['max frequency']:.2f}Mhz")
        print(f"Min Frequency: {cpuInfoDict['min frequency']:.2f}Mhz")
        print(f"Current Frequency: {cpuInfoDict['current frequency']:.2f}Mhz")
        # total usage of cpu
        print(f"Total CPU Usage:{cpuInfoDict['Total CPU Usage']}")
        # Memory Information
        print("=" * 10, "Memory Information", "=" * 10)
        print(f"Total: {getSize(sysMem.total)}")
        print(f"Available: {getSize(sysMem.available)}")
        print(f"Used: {getSize(sysMem.used)}")
        print(f"Percentage: {sysMem.percent}%")
        # ramUsage >>> swap info if exist
        print("=" * 10, "SWAP", "=" * 10)
        print(f"Total: {getSize(swap.total)}")
        print(f"Free: {getSize(swap.free)}")
        print(f"Used: {getSize(swap.used)}")
        print(f"Percentage: {swap.percent}%")
        # for diskinfo >>> diskscanning and info returnning
        print(f"=== Device: {diskInfoDict['device']} ===")
        print(f"  Mountpoint: {diskInfoDict['mountpoint']}")
        print(f"  File system type: {diskInfoDict['file system type']}")
        print(f"  Total Size: {diskInfoDict['Total Size']}")
        print(f"  Used: {diskInfoDict['Used']}")
        print(f"  Free: {diskInfoDict['Free']}")
        print(f"  Percentage: {diskInfoDict['Percentage']}%")
        # diskinfo >>>io counters
        print(f"Total read: {diskIoDict['Total read']}")
        print(f"Total write: {diskIoDict['Total write']}")
        # for netinfo >>> AddressFamily.AF_INET
        print(f"IP Address: {INETdict['IP Address']}")
        print(f"Netmask: {INETdict['Netmask']}")
        print(f"Broadcast IP: {INETdict['Broadcast IP']}")
        # for netinfo >>> AddressFamily.AF_PACKET
        print(f"MAC Address: {PACKETdict['MAC Address']}")
        print(f"Netmask: {PACKETdict['Netmask']}")
        print(f"Broadcast MAC: {PACKETdict['Broadcast MAC']}")
        # for systeminfo >>> general system information
        print(f"sytem name:{sysInfoDict['System']}")
        print(f"name :{sysInfoDict['Name']}")
        print(f" release date of your OS is :{sysInfoDict['Release']}")
        print(f" the system version is :{sysInfoDict['Version']}")
        print(f" machine name :{sysInfoDict['Machine']}")
        print(f" Processor name :{sysInfoDict['Processor']}")
        # system boot info
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

    else:
        pass
    return partList, diskIoList, netIoDict, PACKETdict, INETdict, diskIoDict,
    sysMem, bt, coreList, cpuInfoDict, sysInfoDict, diskInfoDict


def gpuInfo():
    print("="*40, "GPU Details", "="*40)
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
    # get the GPU id
        gpu_id = gpu.id
        # name of GPU
        gpu_name = gpu.name
        # get % percentage of GPU usage of that GPU
        gpu_load = f"{gpu.load*100}%"
        # get free memory in MB format
        gpu_free_memory = f"{gpu.memoryFree}MB"
        # get used memory
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        # get total memory
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))
        userInput = input('if you want to see the info enter p otherwise enter c :')
        if userInput =='p':
            print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                   "temperature", "uuid")))
        else:
            return list_gpus
    return list_gpus


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

