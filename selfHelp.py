import platform
from noche import dic2str

def whoAmI():
	info = {}
	info["platform details"]  = platform.platform()
	info["system name"]= platform.system()
	info["processor name"]  = platform.processor()
	info["architectural detail"] = platform.architecture()
	return dic2str(info)