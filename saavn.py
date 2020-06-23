#!/usr/bin/python3

import json
import requests
import random
from bs4 import BeautifulSoup as z5

et = "\033[92m"
ct = "\033[0m"

lcn = input(et+'\n Enter link of song : '+ct)
qua = (et+"""

	Available Qualities
	[1] 96 => low
	[2] 128 => medium
	[3] 168 => high
	[4] 320 => ultra
"""+ct)

print (qua)
aud = int(input(et+'\n Enter audio resoultion code : '+ct))

grl = requests.get(lcn)
gfl = (grl.content)
tsu = (gfl.decode('utf-8'))
z0f = (z5(tsu, 'html5lib'))
ad0 = (z0f.find_all('script')[42])
foh = ad0.prettify()


for i in foh.split(','):
	if 'pid' in i:
		cv = (i)[9:]

pi = json.loads(cv)
p8 = (pi['pid'])

url = "https://www.jiosaavn.com/api.php"

aex = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/',
	'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
	'Mozilla/5.0 (X11; CrOS x86_64 11895.118.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.159 Safari/537.36',
	'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
	'Mozilla/5.0 (Linux; Android 6.0; CAM-L21 Build/HUAWEICAM-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; Lenovo A7600-F Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
	'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)'
]

for i in range(1, 10):
   user = random.choice(aex)

headers = {
	"Accept":"application/json, text/plain, */*",
	"Accept-Encoding":"gzip, deflate, br",
	"Accept-Language":"en-US,en;q=0.5",
	"Connection":"keep-alive",
	"Host":"www.jiosaavn.com",
	"Referer":"https://www.jiosaavn.com/",
	"TE":"Trailers",
	"User-Agent":user
}

p = {
	"__call":"song.getDetails",
	"pids":p8,
	"api_version":"4",
	"_format":"json",
	"ctx":"web6dot0",
	"_marker":"0"
}

r = requests.get(url, headers=headers, params=p)
rr = (r.content)
r49 = (rr.decode('utf-8'))
w42 = json.loads(r49)
e58 = (w42['songs'][0])
e54 = (e58['title'])
e67 = (e58['subtitle'])
e85 = (e58['more_info'])
r73 = (e85['encrypted_media_url'])

print (et+'\n Song : '+ct, e54)
print (et+'\n sub : '+ct, e67)

po7 = {
	"__call":"song.generateAuthToken",
	"url":r73,
	"bitrate":aud,
	"_format":"json",
	"api_version":"4",
	"_marker":"0",
	"ctx":"web6dot0"
}

rqw = requests.get(url, headers=headers, params=po7)
r3t = (rqw.content)
dp = (r3t.decode('utf-8'))
pd = json.loads(dp)
s3 = (pd['auth_url'])

dx = input('\n do u want to download (y/n) ')

def download():
  if dx == "y":
   try:
       print (et +'\n Downloading!!!!'+ ct)
       sdd = requests.get(s3)
       with open('Song.mp3', 'wb') as pm: 
        pm.write(sdd.content)
       def clear():
         print("\x1B[2J")
       clear()
       print (et +'\n Downloaded !!! '+ ct)
   except KeyboardInterrupt as zre:
       print (et +'\n Abort!!! '+ ct)  
  else:
       print (et +'\n Quiting!! '+ ct)

download()
