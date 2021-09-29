import socket, ssl
from concurrent.futures import ThreadPoolExecutor
import numpy as np


context = ssl.SSLContext()
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

sites=[]

for line in open('potentially_blocked_unique_hostnames.txt','r').readlines():
    sites.append(line.strip())

sites=np.array(sites)
print("List to array complete")
sites=np.array_split(sites,1) #most computers should handle a million domains fine but if you want to do more split the array into more chunks
print("List split complete")
sites=list(sites)

def check_ssl(x):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(s, server_hostname=x)
    ssl_sock.settimeout(3.0) #isp block should reply quickly, thats why timeout is set low
    try:
        ssl_sock.connect(('1.1.1.1', 443))
        ssl_sock.close()
    except ConnectionResetError:
        w = open("blockedsites-kush789-pbw-oracle.txt", "a")
        w.write("\n" + x)
        print( x + " is blocked")
        w.close()
        ssl_sock.close()
    except ssl.SSLCertVerificationError:
        ssl_sock.close()
        pass
    except socket.timeout:
        ssl_sock.close()
        pass
    except Exception as e:
        ssl_sock.close()
        print(e) #print any other exception other than timeout and sslcert error

for z in sites:
    with ThreadPoolExecutor(max_workers=32) as pool:
        response_list = list(pool.map(check_ssl, z))