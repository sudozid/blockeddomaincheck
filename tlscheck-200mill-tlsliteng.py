from tlslite.api import *
from socket import *
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import os
from timeit import default_timer as timer

sitescount=0
timeperthousand=0
def test_tls(domain):
    start_time =  timer()
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(1)
        sock.connect(("1.1.1.1", 443))
        connection = TLSConnection(sock)
        connection.handshakeClientAnonymous(serverName=domain)
    except ConnectionResetError:
        with open("blockedsites-200mill-oracle-new.txt","a") as f:
            f.write(domain+"\n")
        pass
    except:
        pass
    finally:
        end_time = timer()
        global timeperthousand
        timeperthousand=timeperthousand+(end_time-start_time)
        global sitescount
        sitescount+=1
        if(sitescount%1000==0):
            print("Time per thousand: "+str(timeperthousand)+ "Sites done: " + str(sitescount))
            timeperthousand=0
        sock.close()
        connection.close()
        return

for filename in os.listdir('/home/ubuntu/200mill/csvfiles/'):
    sites = []
    with open(os.path.join('/home/ubuntu/200mill/csvfiles/',filename)) as f:
        for line in f:
         sites.append(line.strip())
    sites=np.array_split(sites,5)
    for y in sites:
        with ThreadPoolExecutor(max_workers=75) as pool:
           pool.map(test_tls, y)
