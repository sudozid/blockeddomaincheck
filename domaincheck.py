import csv
import requests
from concurrent.futures import ThreadPoolExecutor
import re
sites=[]

requests.packages.urllib3.disable_warnings()

with open('majestic_million.csv', 'r',encoding = 'cp850') as rf:
 reader = csv.reader(rf)
 for i in reader:
    sites.extend([i[2]]) #domain is in 3rd column of csv file

sites.pop(0) #remove column header

def get_url(x):
  x="http://"+x
  try:
   y=requests.get(x,timeout=1,allow_redirects=False, verify=False)
  except:
   pass
  try:
   regexp = re.compile(r'\<iframe src\=\"http\:\/\/.*:8080\/webadmin\/deny\/index\.php')
   if regexp.search(y.text):
    w = open("blockedsites.txt", "a")
    w.write("\n" + y.url)
    print(y.url + "is blocked")
    w.close()
  except:
   pass

#change max_workers to request many sites at once
#keep in mind your router may not be able to handle it if u set too high
with ThreadPoolExecutor(max_workers=4) as pool:
 response_list = list(pool.map(get_url, sites))
