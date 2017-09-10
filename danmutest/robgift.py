# -*- coding: UTF-8 -*-

import time, urllib,   threading,   winsound 
import bilibilicookie
from danmu import DanMuClient
danmu_rnd = int(time.time())
 
def bbbb():
    winsound.Beep(600,500)
    winsound.Beep(300,500)
    winsound.Beep(900,500)
    

def sendDanmu(realroomid, msg, test = False):
    
    url = "http://api.live.bilibili.com/msg/send" 
    
    
    postdata=urllib.parse.urlencode({  
              "roomid":realroomid,  
              "rnd": danmu_rnd,
              "msg": msg,
              "color": 16777215,
              "fontsize": 25,
              "mode" : 1,
              
              
                    }).encode('utf-8') 
    
    
    header={
        "Accept":" */*",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection":"keep-alive",
        "Cookie": bilibilicookie.nowcookie,
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Host":"api.live.bilibili.com",
        "Origin":"http://static.hdslb.com",
        "Referer": "http://static.hdslb.com/live-static/swf/LivePlayerEx_1.swf?_=1-1-1.1.0",
        "User-Agent":bilibilicookie.nowagent,
        "X-Requested-With" : "ShockwaveFlash/26.0.0.151",       
        }
    
    
    print('try send danmu',realroomid, msg)
    
    
    print(url)
    print(postdata)
    #print(header)
    
    req = urllib.request.Request(url,postdata,header)
    
    if (test):
        return
    
    r=urllib.request.urlopen(req)
    re = r.read().decode('utf-8')
    print(re)
    return re



danmulist = {}

danmumutex = threading.Lock() 

def printtime(t = None):
        if (t is None) : t = time.time()
        localtime = time.localtime(t)
        ts = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
        return ts


def moniterDanmu(url, lasttime  = 100):
    
    if (url == "http://live.bilibili.com/356767") :
        print ( 'moniterDanmu  same  return ',  url)
        return
    
    nowt = time.time()
    
    danmumutex.acquire()
    try:
        if (url in danmulist) :
            (d,t) = danmulist[url]
            danmulist[url] = (d, nowt + lasttime)
            
            print('extend moniter', url, printtime(nowt))
        else :
            d = DanMuClient(url)
            d.start(blockThread = False)
            danmulist[url] = (d, nowt + lasttime)
            print('start moniter', url, printtime(nowt))
    except Exception as e:
        print(e)
        
    danmumutex.release()

    

def work():
    print("enter danmu work")
    while True:
        time.sleep(10)
        nowt = time.time()
        
        if not danmumutex.acquire(500): continue
        keys = danmulist.keys()
        
        pt = []
        
        for key in keys :
            (d,t) = danmulist[key]
            if (t  < nowt) :
                d.stop()
                pt.append(key)
                print('end moniter', key, printtime(nowt))
                
        for x in pt :
            danmulist.pop(x)
        danmumutex.release()

danmuthread = threading.Thread(target=work)
danmuthread.setDaemon(True)
danmuthread.start()
        
            
if __name__ == "__main__":
    print('robgift!!!!!!!!!!!!!!!!!!!!')
    
    moniterDanmu("http://live.bilibili.com/82789", 15)
    
    while True:
        print(time.time())
        time.sleep(10)
        
                    