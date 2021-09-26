"""
Network
"""
import requests
import re




def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                       'https': 'socks5h://127.0.0.1:9050'}
    ret=""
    success="This browser is configured to use Tor"
    try:
        ret=session.get("https://check.torproject.org/").text
        if  success in ret:
            print("TorBala Got a session")
            return session
        else:
            print("deadend")
    except Exception as e:
        print(e)
    return session


def getHTML(url,secure=0):
    print(secure)
    session=""
    if secure>0:
        session=get_tor_session()
        print("Tor On:{}".format(url))
    elif secure<1 :
        session=requests.session()
        print("IRTCI:{}".format(url))
    try:
        return session.get(url).text  #content.capitalize()
    except Exception as e:
        print (e)
        return "[ERROR]"+str(e)


