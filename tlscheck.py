import socket, ssl
import csv
from concurrent.futures import ThreadPoolExecutor

context = ssl.SSLContext()
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

sites=[]

with open('majestic_million.csv', 'r',encoding = 'cp850') as rf:
 reader = csv.reader(rf)
 for i in reader:
    sites.extend([i[2]]) #domain is in 3rd column of csv file
print("File open done")
sites.pop(0) #remove column header

def check_ssl(x):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(s, server_hostname=x)
    try:
        ssl_sock.connect(('1.1.1.1', 443))
        ssl_sock.close()
    except ConnectionResetError:
        w = open("blockedsites4.txt", "a")
        w.write("\n" + x)
        print( x + " is blocked")
        w.close()
    except:
        pass

with ThreadPoolExecutor(max_workers=40) as pool:
 response_list = list(pool.map(check_ssl, sites))
