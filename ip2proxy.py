
import IP2Proxy

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

    print (versionDict['Module Version'])
    print (versionDict['Package Version'])
    print (versionDict['Database Version'])

    #return a dict of info 
    record = db.get_all(proxyip)

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

    # close IP2Proxy BIN database
    db.close()

    # Web Service
    ws = IP2Proxy.IP2ProxyWebService("demo","PX11",True)
    rec = ws.lookup("89.208.35.79")
    print ("\n")
    print ("Credit Remaining: {}\n".format(ws.getcredit()))

# individual proxy data check
    # print ('Is Proxy: ' + str(db.is_proxy(proxyip)))
    # print ('Proxy Type: ' + db.get_proxy_type(proxyip))
    # print ('Country Code: ' + db.get_country_short(proxyip))
    # print ('Country Name: ' + db.get_country_long(proxyip))
    # print ('Region Name: ' + db.get_region(proxyip))
    # print ('City Name: ' + db.get_city(proxyip))
    # print ('ISP: ' + db.get_isp(proxyip))
    # print ('Domain: ' + db.get_domain(proxyip))
    # print ('Usage Type: ' + db.get_usage_type(proxyip))
    # print ('ASN: ' + db.get_asn(proxyip))
    # print ('AS Name: ' + db.get_as_name(proxyip))
    # print ('Last Seen: ' + db.get_last_seen(proxyip))
    # print ('Threat: ' + db.get_threat(proxyip))
    # print ('Provider: ' + db.get_provider(proxyip))

    # single function to get all proxy data returned in array
    # this returns a dict