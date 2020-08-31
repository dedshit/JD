#!/usr/bin/python3
import requests
import sys
import argparse
import bs4
import headers
def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--A", help="Enter audio ", action="store_true")
    parser.add_argument("-q", action="store_true")
    args, unknown = parser.parse_known_args()
def sig():
    try:
        if sys.argv[1] == '-a' or '--A':
            req = requests.get(sys.argv[2])
            req_parse = bs4.BeautifulSoup(req.content.decode(), "html5lib")
            content = req_parse.find_all("script")[40].prettify()
            pi = []
            for _ in content.split(','):
                if "pid" in _:
                    pi.append(_)
            pid = eval((pi[0])[9:])['pid']
            return pid   
        else:
            pass
    except IndexError:
        pass
def song():
    data = {
        "__call":"song.getDetails",
        "pids":sig(),
        "api_version":"4",
        "_format":"json",
        "ctx":"web6dot0",
        "_marker":"0"
    }
    req = requests.get("https://www.jiosaavn.com/api.php", headers=headers.headers, params=data)
    pr = (req.json())
    try:
        if sys.argv[3]:
            pix = int(sys.argv[4])
            x1 = pr["songs"][0]["title"]
            print("SONG : ", x1)
            enc_url = pr["songs"][0]["more_info"]["encrypted_media_url"]
            data = {
                "__call":"song.generateAuthToken",
                "url":enc_url,
                "bitrate":pix,
                "_format":"json",
                "api_version":"4",
                "_marker":"0",
                "ctx":"web6dot0"
            }
            song_req = requests.post("https://www.jiosaavn.com/api.php", headers=headers.headers, data=data)
            tokn_url = (song_req.json()["auth_url"])
            dl = requests.get(tokn_url)
            with open('{}.mp3'.format(x1), "wb") as jn:
                jn.write(dl.content)
        else:
            pass            
    except IndexError:
        print("python3 saavn.py { -a/--A <song> -q <pixel> <-}")
    except KeyboardInterrupt:
        print("Abort")
if __name__ == "__main__":
    song()
