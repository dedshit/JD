#!/usr/bin/python3

import requests
import json
import os
from bs4 import BeautifulSoup as bx
import random
import sys

et = '\033[92m'
ct = '\033[0m'

sys.stdout.write(et +'\n Enter song link : '+ ct)
link = sys.stdin.readline()
aud = input(et +'\n Enter Quality (default:192) : '+ ct)

if aud:
   try:
      print (et +'\n setting to %s' %aud + ct)
   except ValueError:
      print ('')
   except KeyboardInterrupt:
      print ('\n abort')

def req():
  a1 = requests.get(link)
  if a1.status_code == 200:
    b1 = (a1.content.decode())
    c1 = (bx(b1, 'html5lib'))
    x7 = (c1.find('h1', class_="u-h2 u-ellipsis@lg u-margin-bottom-tiny@sm")).text
    print (et +'\n Song : '+ ct,x7)
    d1 = (c1.find_all('script')[40])
    e1 = (d1.prettify())
    f1 = bytes(e1.encode())
    with open('w2.txt', 'wb') as c:
     c.write(f1)
  else:
    print ('\n Check ur connection and try again')
req()


with open('w2.txt') as f:
	for i in f.read().split(','):
		if 'encrypted_media_url' in i:
			v = (i[23:-1])

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

url = "https://www.jiosaavn.com/api.php"

h = {
 	'Host': 'www.jiosaavn.com',
        'User-Agent': user,
        'Accept': 'application/json, text/plain, */*',
	'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers'
}

p = {
	'url': v,
	'__call': 'song.generateAuthToken',
	'_marker': '0',
	'_format': 'json',
	'bitrate': aud,
	'api_version': '4',
	'ctx': 'web6dot0'
}

r = requests.post(url, headers=h, data=p)
r2 = (r.content)

with open('w3.txt', 'wb') as z:
	z.write(r2)
with open('w3.txt') as x:
	da1 = json.load(x)
z1 = (da1['auth_url'])

dx = input(et +'\n Do u want to download  Song {y/n}: '+ ct)

def download():
  if dx == "y":
   try:
       print (x7)
       print (et +'\n Downloading!!!!'+ ct)
       sdd = requests.get(z1)
       with open('Song.mp3', 'wb') as pm:
        pm.write(sdd.content)
       os.system('clear')
       print (et +'\n Downloaded !!! '+ ct)
       trx = "$HOME/jio-saavu-downloader/Saavn/*.txt"
       os.system('rm -rf %s' % trx)
   except KeyboardInterrupt as zre:
       print (et +'\n Quittin!!! '+ ct)
  else:
       print (et +'\n Quiting!! '+ ct)
       xfq = "$HOME/jio-saavu-downloader/Saavn/*.txt"
       os.system('rm -rf %s' % xfq)
download()

