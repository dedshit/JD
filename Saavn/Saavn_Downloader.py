#!/usr/bin/python3

from bs4 import BeautifulSoup as z
import requests
import json
import time
import sys
import os

#color:
et = '\033[92m'
ct = '\033[0m'

sys.stdout.write(et +'\n Enter link : '+ ct)
sys.stdout.flush()
link = sys.stdin.readline()
bit = int(input(et +'\n Enter bitrate( default:256 ) : '+ ct))
 
#Fuk(off):
#Copying won't make u Coder:

dr = requests.get(link)
with open('err.txt', 'wb') as h:
	h.write(dr.content)
with open('err.txt') as x:
	s = z(x, 'html5lib')
qq = s.find_all('div', id="header")[0]
qp = qq.find('div', class_="hide song-json").next
sk = bytes(qp.encode())
time.sleep(2)

def identify():
  x1rs = qq.find('div', class_="header-content").h1
  print (et +'\n Name : '+ ct, x1rs.text) 
  srh = s.find_all('div', class_="details content-list")[0]
  rsh = srh.find('p', class_="album-name ellip").next
  print (et +'\n Album : '+ ct, rsh) 
  dw = s.find_all('p', id="timer")[0]
  wd = dw.text
  print (et +'\n Duration : '+ ct, wd) 
  time.sleep(2)
identify()


with open('j.txt', 'wb') as q1:
	q1.write(sk)
with open('j.txt') as zz:
	ass = json.load(zz)
q2 = (ass['url'])

url = "https://www.jiosaavn.com/api.php"

headers = {
	'Host': 'www.jiosaavn.com',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Content-Length': '180',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'Cache-Control': 'max-age=0',
	'TE': 'Trailers'
}

pa = {
       	'url': q2,
	'__call': 'song.generateAuthToken',
	'_marker': 'false',
	'_format': 'json',
	'bitrate': bit
}

r = requests.post(url, headers=headers, data=pa)

with open('dy.txt', 'wb') as f:
	f.write(r.content)
with open('dy.txt') as c:
	rr = json.load(c)
dre = (rr['auth_url'])
dx = input(et +'\n Do u Need to download this Song ?? {y/n}: '+ ct)
 
def download():
  if dx == "y":
   try:
       print (et +'\n Downloading!!!!'+ ct) 
       rl_1 = dre
       sdd = requests.get(rl_1)
       with open('song.mp3', 'wb') as pm:
        pm.write(sdd.content)
       print (et +'\n Downloaded !!! '+ ct)
       trx = "$HOME/jio-saavu-downloader/Saavn/*.txt" 
       os.system('rm -rf %s' % trx)
   except KeyboardInterrupt as zre:
       print (et +'\n Quittin!!! '+ ct)
  else:  
       print (et +'\n bye!! '+ ct)
       xfq = "$HOME/jio-saavu-downloader/Saavn/*.txt"
       os.system('rm -rf %s' % xfq)
download()
