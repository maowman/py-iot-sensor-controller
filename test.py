import requests
from bs4 import BeautifulSoup
req=requests.get("http://192.168.4.1/value")
bsobj=BeautifulSoup(req.text,features="html5lib")
table=bsobj.find_all("font")
print(table)
print(table[2].get_text())
print(table[4].get_text())
print(table[6].get_text())