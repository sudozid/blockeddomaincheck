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

for filename in os.listdir('/home/ubuntu/blockeddomaincheck/200mill/csvfiles'):
    sites = []
    with open(os.path.join('/home/ubuntu/blockeddomaincheck/200mill/csvfiles',filename)) as f:
        for line in f:
            if(line=="" or line is None):
                pass
            else:
                sites.append(line.strip())
    print(filename + "Opened")

    sites=np.array(sites)
    print("List to array complete")
    sites=np.array_split(sites,2) #most computers should handle a million domains fine but if you want to do more split the array into more chunks
    print("List split complete")
    sites=list(sites)

    def check_ssl(x):
        if x=="" or x is None:
         pass
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = context.wrap_socket(s, server_hostname=x)
        ssl_sock.settimeout(3.0) #isp block should reply quickly, thats why timeout is set low
        try:
            ssl_sock.connect(('1.1.1.1', 443))
            ssl_sock.close()
        except ConnectionResetError:
            w = open("blockedsites-200mill-oracle.txt", "a")
            w.write("\n" + x)
            w.close()
            ssl_sock.close()
        except ssl.SSLCertVerificationError:
            ssl_sock.close()
            pass
        except socket.timeout:
            l=open("blockedsites-200mill-oracle-timeout.txt","a") #add all timeouts to a text file to be rechecked later
            l.write("\n"+x)
            l.close()
            ssl_sock.close()
            pass
        except Exception as e:
            # add all other exceptions to a text file to be rechecked later
            m=open("blockedsites-200mill-oracle-otherexception.txt","a")
            m.write("\n"+x)
            m.close()
            ssl_sock.close()
        except:
            pass

    for z in sites:
        with ThreadPoolExecutor(max_workers=20) as pool:
            response_list = list(pool.map(check_ssl, z))