from reels_downloader.main.Reels import Reels
import config as conf
import re
import requests

async def get_reel_id(link):
    match = re.findall(r"https:\/\/www\.instagram\.com\/(reel|reels)\/(.*)\/(.*)", link)
    reel_id = str(match[0][1])
    if match != None: 
        return reel_id
    else:
        return "err"

async def download_reel(link):
    my_reel = Reels(conf.SESSION_ID)
    reel_id = await get_reel_id(link)
    if reel_id != "err":
        info = await my_reel.get(reel_id)
        fstream = requests.get(info.videos[0].url).content
        return "OK", fstream
    else:
        return "ERR"