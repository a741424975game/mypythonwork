# -*- coding: UTF-8 -*-

import time, urllib,   threading,   winsound, requests, json , re
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
    result = r.read().decode('utf-8')
    print(result)
    return result


def sendGift(realroomid, giftId, giftNum, giftBagId):
    
    url = "http://api.live.bilibili.com/giftBag/send" 
    
    token = re.findall('LIVE_LOGIN_DATA=(.*?);', bilibilicookie.nowcookie)[0] 
    
    timestamp = str(int( time.time() * 1000) )  
    postdata=urllib.parse.urlencode({  
              "giftId": giftId,
              "roomid":realroomid,  
              "ruid": 2013332,
              "num": giftNum,
              "coinType" : "silver",
              "Bag_id" : giftBagId,
              "timestamp" : timestamp,
              "rnd": danmu_rnd,
              "token" : token

              
              
                    }).encode('utf-8') 
    
    
    header={
        "Accept":" */*",
        #"Accept-Encoding":"gzip, deflate",
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
    
    
    print('try send gift',realroomid, giftId, giftNum, giftBagId)
    
    
    print(url)
    print(postdata)
    #print(header)
    
    req = urllib.request.Request(url,postdata,header)
    
    r=urllib.request.urlopen(req)
    result = r.read().decode('utf-8')
    print(result)
    return result


def getGiftBag():
    
    timestamp = str(int( time.time() * 1000) )  
    url  = "http://api.live.bilibili.com/gift/playerBag?_=" + timestamp
    print(url)
    
    header={
        "Accept":"application/json, text/javascript, */*; q=0.01",
        #"Accept-Encoding":"gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection":"keep-alive",
        "Cookie": bilibilicookie.nowcookie,
        
        "Host":"api.live.bilibili.com",
        "Origin":"http://live.bilibili.com",
        "Referer": "http://live.bilibili.com/356767",
         
        "User-Agent":bilibilicookie.nowagent,
                
        }
     
    
    req = urllib.request.Request(url,None,header)
    
    r=urllib.request.urlopen(req)
    result = r.read().decode('utf-8')
    print(result)
    
    try:
        jo = json.loads(result)
        data  = jo["data"]
        if ( len(data) ==0): return []
        return data
    except Exception as e:
        print(e)
        return []


def dosign():
     
    url  = "http://api.live.bilibili.com/sign/doSign"
    print(url)
    
    header={
        "Accept":"application/json, text/javascript, */*; q=0.01",
 
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection":"keep-alive",
        "Cookie": bilibilicookie.nowcookie,
        
        "Host":"api.live.bilibili.com",
        "Origin":"http://live.bilibili.com",
        "Referer": "http://live.bilibili.com/356767",
         
        "User-Agent":bilibilicookie.nowagent,
                
        }
     
    
    req = urllib.request.Request(url,None,header)
    
    r=urllib.request.urlopen(req)
    result = r.read().decode('utf-8')
    print(result)
    
 
def checkUnionRank():
     
    url  = "http://api.live.bilibili.com/activity/v1/UnionFans/getFansList?page=[page]&type=other"

    header={
        "Accept":"application/json, text/javascript, */*; q=0.01",
 
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection":"keep-alive",
        "Cookie": bilibilicookie.nowcookie,
        
        "Host":"api.live.bilibili.com",
        "Origin":"http://live.bilibili.com",
        "Referer": "http://live.bilibili.com/356767",
         
        "User-Agent":bilibilicookie.nowagent,
                
        }
     
     
    pool = []
     
    for ii in range(1,100) :
        u = url.replace( "[page]",  str(ii))
        #print(u)
        req = urllib.request.Request(u,None,header)
        r=urllib.request.urlopen(req)
        result = r.read().decode('utf-8')
        #print(result)    
        
        jo = json.loads(result)
        data = jo['data']
        
        ll = data['list']
        pool.extend(ll)
        
        tp  = data['totalPage'];
        tp = int(tp)
        if (tp == ii): break;
    
    me = 0;    
    for x in pool :
        #print(x)
        if int (x['uid']) == 82778:
            me = x['weekly_score']
            break;
    count = 0;
    for x in pool :
        n = x['weekly_score']
        if me <= n : 
            print(x)
            count+=1
    print("count ", count)
    return count
    
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

    

def moniterendwork():
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


        
        
def giftmoniter():
    
    print("enter giftmoniter")
    
    while True:
        try:
            print("try sign")
            dosign()
            time.sleep(5)
        except Exception as e:
            print(e)
        try:
            print("check gift bag")
            gb = getGiftBag()
            for x in gb:
                if x['expireat'] == '今日':
                    print('send gift')
                    sendGift(356767, x['gift_id'], x['gift_num'], x['id'])
                    time.sleep(1)
        except Exception as e:
            print(e)
            
        time.sleep(3600 * 4)
        
def getexpireat(s):
    if s == '今日':
        return 1
    if s == '明日' or s=='明天':
        return 2
    if s== '永久':
        return 9999
    try:
        x = s.find('天')
        if x>=0 :
            return int(s[0:x])
    except Exception as e:
        print(e)
        
    return 99
def getOneGift() :
    gb = getGiftBag()
    target = None
    tt = 999
    for x in gb:
        t = getexpireat(x['expireat'])
        if (t<tt) :
            tt = t
            target = x
    return target

def catchrank():
    print("try checkUnionRank  ")
    while(1) :
        count = checkUnionRank()
        if (count >5) :
            x = getOneGift()
                    
            if x != None:
                print('send gift')
                sendGift(356767, x['gift_id'], x['gift_num'], x['id'])
                time.sleep(5)
                continue
         
        break;    

def unionmoniter():
    
    print("enter unionmoniter")
    
    while True:
        sleeptime = 30
        
        localtime = time.localtime(time.time())
        if localtime.tm_wday != 4  :
            sleeptime = 3600*4
        else :
            if  localtime.tm_hour!= 19 or localtime.tm_min<50:
                time.sleep(sleeptime)
                continue
            
        try:
            catchrank()

            
        except Exception as e:
            print(e)    
            
        time.sleep(sleeptime)

if   __name__ != "__main__":
    danmuthread = threading.Thread(target=moniterendwork)
    danmuthread.setDaemon(True)
    danmuthread.start()
       
    danmuthread1 = threading.Thread(target=giftmoniter)
    danmuthread1.setDaemon(True)
    danmuthread1.start()   

    danmuthread2 = threading.Thread(target=unionmoniter)
    danmuthread2.setDaemon(True)
    danmuthread2.start()  
            
if __name__ == "__main__":
    print('robgift!!!!!!!!!!!!!!!!!!!!')
    catchrank()
    exit()
    checkUnionRank()
    x = getOneGift()
    print(x)
    exit()    
    
    giftmoniter()
    exit()
    
    
    exit()
    x = re.findall('LIVE_LOGIN_DATA=(.*?);', bilibilicookie.nowcookie)[0] 
    print(x)
    
    print(1111)
    #sendGift(356767,1,1,44385613 )
    #dosign()
    print(2222)
    
    x = getGiftBag()
    print(x)
    
    #sendDanmu(82789, "asdfadfasdfasf");
    
    #moniterDanmu("http://live.bilibili.com/82789", 15)
    
    
    
    while True:
        print(time.time())
        time.sleep(10)
        
        

            