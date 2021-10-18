from multiprocessing import Pool
import socket, ssl
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import os

context = ssl.SSLContext()
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

"""
csvfiles will contain over 260million domains to be checked
the csv file must be split into over 100 files with 2 million domains each
use "split -l2000000 200milliondomains.csv" on linux to split it this way
"""
b=0
for filename in os.listdir('/home/ubuntu/blockeddomaincheck/200mill/csvfiles/'):
    sites=[]
    b=b+1
    print(b)
    with open(os.path.join('/home/ubuntu/blockeddomaincheck/200mill/csvfiles/',filename)) as f:
        for line in f:
         sites.append(line.strip())
    print(filename + "Opened")
    def check_ssl(x):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
         ssl_sock = context.wrap_socket(s, server_hostname=x)
        except UnicodeError:
         print(x + " unicode error")
         return
        ssl_sock.settimeout(3.0) #isp block should reply quickly, thats why timeout is set low
        try:
            ssl_sock.connect(('1.1.1.1', 443))
            ssl_sock.close()
        except ConnectionResetError:
            with open("blockedsites-200mill-oracle.txt", "a") as w:
             w.write("\n" + x)
            print(x)
            ssl_sock.close()
        except ssl.SSLCertVerificationError:
            ssl_sock.close()
            return
        except socket.timeout:
            with open("blockedsites-200mill-oracle-timeout.txt","a") as v: #add all timeouts to a text file to be rechecked later
             v.write("\n"+x)
            ssl_sock.close()
            return
        except Exception as e:
            # add all other exceptions to a text file to be rechecked later
            with open("blockedsites-200mill-oracle-otherexception.txt","a") as m:
             m.write("\n"+x)
            ssl_sock.close()
            return
    with ThreadPoolExecutor(max_workers=30) as pool:
     pool.map(check_ssl, sites)
