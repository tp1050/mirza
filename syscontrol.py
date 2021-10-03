import re
import psutil
import platform
# for gpu 
import GPUtil
from tabulate import tabulate
from datetime import datetime

def getSize(bytes, suffix='B'):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor 

# system information 
def sysInfo():
    uname = platform.uname()
    sysinfo = {
        'System':uname.system,
        'Name': uname.node,
        'Release' : uname.release,
        'Version' : uname.version,
        'Machine' : uname.machine,
        'Processor' : uname.processor
    }
    print(f"sytem name:{sysinfo['System']}")
    print(f"name :{sysinfo['Name']}")
    print(f" release date of your OS is :{sysinfo['Release']}")
    print(f" the system version is :{sysinfo['Version']}")
    print(f" machine name :{sysinfo['Machine']}")
    print(f" Processor name :{sysinfo['Processor']}")

# boz =sysinfo.items()
def boot_time():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    return f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"

def cpuInfo():
    cpuFreq =psutil.cpu_freq()
    cpuInfoDict ={
        'physical cores' : psutil.cpu_count(logical=False),
        'total cores' : psutil.cpu_count(logical=True),
        'current frequency' : cpuFreq.current ,
        'max frequency': cpuFreq.max,
        'min frequency' : cpuFreq.min,
        'Total CPU Usage' : psutil.cpu_percent()
    }
    print(f"Max Frequency: {cpuInfoDict['max frequency']:.2f}Mhz")
    print(f"Min Frequency: {cpuInfoDict['min frequency']:.2f}Mhz")
    print(f"Current Frequency: {cpuInfoDict['current frequency']:.2f}Mhz")
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage:{cpuInfoDict['Total CPU Usage']}")
def ramUsage():
    sysmem = psutil.virtual_memory()
    # Memory Information
    print("="*40, "Memory Information", "="*40)
    # get the memory details
    sysmem = psutil.virtual_memory()
    print(f"Total: {getSize(sysmem.total)}")
    print(f"Available: {getSize(sysmem.available)}")
    print(f"Used: {getSize(sysmem.used)}")
    print(f"Percentage: {sysmem.percent}%")
    print("="*20, "SWAP", "="*20)
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"Total: {getSize(swap.total)}")
    print(f"Free: {getSize(swap.free)}")
    print(f"Used: {getSize(swap.used)}")
    print(f"Percentage: {swap.percent}%")



def diskInfo():
    partitions = psutil.disk_partitions()
    partList=[]
    diskIoList=[]
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            print('this can be catched due to the disk that isnt ready')
            continue
        diskInfoDict = {
            'device' : partition.device ,
            'mountpoint' : partition.mountpoint ,
            'file system type' : partition.fstype ,
            'Total Size': getSize(partition_usage.total) ,
            'Used': getSize(partition_usage.used),
            'Free': getSize(partition_usage.free) ,
            'Percentage': f"  Percentage: {partition_usage.percent}%" ,
        }
        print(f"=== Device: {diskInfoDict['device']} ===")
        print(f"  Mountpoint: {diskInfoDict['mountpoint']}")
        print(f"  File system type: {diskInfoDict['file system type']}")
        print(f"  Total Size: {diskInfoDict['Total Size']}")
        print(f"  Used: {diskInfoDict['Used']}")
        print(f"  Free: {diskInfoDict['Free']}")
        print(f"  Percentage: {diskInfoDict['Percentage']}%")
        partList.append(diskInfoDict)

    diskIo = psutil.disk_io_counters()
    for disk in diskIo:
        try:
            diskIoDict ={
                'Total read': getSize(diskIo.read_bytes),
                'Total write': getSize(diskIo.write_bytes),
            }
        except Exception as e:
            print('oops accessing disk_io_counters hit a wall')

        diskIoList.append(diskIoDict)
    print(f"Total read: {diskIoDict['Total read']}")
    print(f"Total write: {diskIoDict['Total write']}")

    return partList , diskIoList

    
diskInfo()

def network():
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                INETdict={
                 'IP Address' : address.address ,
                 'Netmask' : address.netmask ,
                 'Broadcast IP' : address.broadcast ,
                }
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                PACKETdict = {
                 'MAC Address' :address.address ,
                 'Netmask' :address.netmask,
                 'Broadcast MAC' :address.broadcast,
                }
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    netIoDict ={
        'Total Bytes Sent' : getSize(net_io.bytes_sent),
        'Total Bytes Received' : getSize(net_io.bytes_recv),
    }
    # for AddressFamily.AF_INET
    print(f"IP Address: {INETdict['IP Address']}")
    print(f"Netmask: {INETdict['Netmask']}")
    print(f"Broadcast IP: {INETdict['Broadcast IP']}")
    # for AddressFamily.AF_PACKET 
    print(f"MAC Address: {PACKETdict['MAC Address']}")
    print(f"Netmask: {PACKETdict['Netmask']}")
    print(f"Broadcast MAC: {PACKETdict['Broadcast MAC']}")

# gpu info 
# GPU information

# print("="*40, "GPU Details", "="*40)
# gpus = GPUtil.getGPUs()
# list_gpus = []
# for gpu in gpus:
#     # get the GPU id
#     gpu_id = gpu.id
#     # name of GPU
#     gpu_name = gpu.name
#     # get % percentage of GPU usage of that GPU
#     gpu_load = f"{gpu.load*100}%"
#     # get free memory in MB format
#     gpu_free_memory = f"{gpu.memoryFree}MB"
#     # get used memory
#     gpu_used_memory = f"{gpu.memoryUsed}MB"
#     # get total memory
#     gpu_total_memory = f"{gpu.memoryTotal}MB"
#     # get GPU temperature in Celsius
#     gpu_temperature = f"{gpu.temperature} °C"
#     gpu_uuid = gpu.uuid
#     list_gpus.append((
#         gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
#         gpu_total_memory, gpu_temperature, gpu_uuid
#     ))

# print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
#                                    "temperature", "uuid")))

def narin():
    for i in range(20):
        print('=',end='')

sysInfo()
narin()
boot_time()
narin()
cpuInfo()
narin()
ramUsage()
narin()
diskInfo()
narin()
network()
