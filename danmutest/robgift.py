# -*- coding: UTF-8 -*-

import time, urllib, random, threading, json, winsound, requests

danmu_rnd = int(time.time())
nowcookie = "pgv_pvi=1496014848; fts=1442990593; pgv_si=s5590225920; sid=80to18h9; _ga=GA1.2.18888997.1484058402; rpdid=olppqsqqsqdopqpwsqxxw; UM_distinctid=15ab6d5631d4c0-0a7e8799ef7e7e-6b1b1279-13c680-15ab6d5631e772; X-Through=Live-Api-Async; HTML5PlayerCRC32=2961144679; biliMzIsnew=1; biliMzTs=0; finger=edc6ecda; _cnt_dyn=0; uTZ=-480; _qddaz=QD.w4rad5.jh22gx.j6llthjw; buvid3=81BAB62C-CA0D-401C-85F9-092D47752AEC31597infoc2; DedeUserID=82778; DedeUserID__ckMd5=db22cc81b5150e95; SESSDATA=3dc3d386%2C1506477612%2Cdf19d0db; bili_jct=8f1072e39a68b7e9d0a58aed8f238fe0; _cnt_pm=1; _cnt_notify=32; LIVE_BUVID=903b962a52c4623f1c12599141e41431; LIVE_BUVID__ckMd5=13629ba9215dd5a9; LIVE_LOGIN_DATA=14d06d18c269ef6d0e73ce529f4c129781e93b22; LIVE_LOGIN_DATA__ckMd5=37a8c88983b4abb5; _dfcaptcha=5964dacfc2954105b64936c2d8c9cb08; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1503978394,1503978397,1503980903,1503981276; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1504083791"
nowagent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"


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
    
    print(postdata)
    
    header={
        "Accept":" */*",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection":"keep-alive",
        "Cookie": nowcookie,
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Host":"api.live.bilibili.com",
        "Origin":"http://static.hdslb.com",
        "Referer": "http://static.hdslb.com/live-static/swf/LivePlayerEx_1.swf?_=1-1-1.1.0",
        "User-Agent":nowagent,
        "X-Requested-With" : "ShockwaveFlash/26.0.0.151",       
        }
    
    
    print('try send danmu')
    
    
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

def robBeatstorm(msg):
#url = ('http://live.bilibili.com/'
#+ self.url.split('/')[-1] or self.url.split('/')[-2])
#self.roomId = re.findall(b'var ROOMID = (\d+);', requests.get(url).content)[0].decode('ascii')
    try:
        x =  msg['data']['39']
        content = x['content']
    except:
        print ("rob beatstorm error")
        return

    sendDanmu(356767, content)
    
    return

def robtv(roomurl, realroomid, tvid, test = False):
    
    
    print('try rob tv')
    
    delay =  random.randint(5000, 8000)
    if  test is False :
        print('delay', delay)
        time.sleep( delay/ 1000.0)
    
    realroomid = int(realroomid)
    tvid = int(tvid)
    timestamp = int( time.time() * 1000)  
    url = "http://api.live.bilibili.com/SmallTV/join?roomid=%d&id=%d&_=%d" % (realroomid, tvid, timestamp)
    
    
    #postdata=urllib.parse.urlencode({        "JobName":"测试工程师",        }).encode('utf-8')
    
    header={
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection":"keep-alive",
        "Cookie": nowcookie,
        
        "Host":"api.live.bilibili.com",
        "Origin":"http://live.bilibili.com",
        "Referer": roomurl,
         
        "User-Agent":nowagent,
                
        }
    
    print(url)
    #print(header)
    
    req = urllib.request.Request(url,None,header)
    
    print(req)
        
    if test:
        return ""
    
    r=urllib.request.urlopen(req)
    re = (r.read().decode('utf-8'))
    print(re)
    return re
    
    
def robstudy(roomurl, realroomid,   test = False):
    
    
    delay =  random.randint(2000, 4000)
    if  test is False :
        time.sleep( delay/ 1000.0)
     
    realroomid = str(realroomid)
    
    data = []
    try:
        re = requests.get("http://api.live.bilibili.com/activity/v1/SchoolOpen/check?roomid=" +  (realroomid))
        x = json.loads(re)
        data = x['data']
    except:
        print('get study list fail ')
        print (re)
        return False
    print(data)
    
    if (type(data) != list):
        return False
    
    for target in data:
        try:
            #{"code":0,"msg":"success","message":"success",
            #"data":[{"raffleId":"27279","type":"school","from":"黑丝细腿","time":38,"status":1}]}
            url = "http://api.live.bilibili.com/activity/v1/SchoolOpen/join" 
            raffleId = target['raffleId']
            status = target['status']
            if (status != 1):
                print ('already inside')
                continue
            postdata=urllib.parse.urlencode({  
                      "roomid":realroomid,  
                      "raffleId": raffleId
                            }).encode('utf-8')
            
            header={
                "Accept":"application/json, text/javascript, */*; q=0.01",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.8",
                "Connection":"keep-alive",
                "Cookie":nowcookie,
                "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Host":"api.live.bilibili.com",
                "Origin":"http://live.bilibili.com",
                "Referer": roomurl,
                 
                "User-Agent":nowagent,
                        
                }
            
            print('try rob study')
            print(postdata)
            
            req = urllib.request.Request(url,postdata,header)
            
            r=urllib.request.urlopen(req)
            print(r.read().decode('utf-8'))
            
            time.sleep( 0.1)
            
        except Exception as e:
            print("fail rob study one")
            print (e)
    return True
    
    
def isTv(msg):
    try:
        if ('tv_id' in msg):
            return True
    except:
        pass
    
    return False
      
def isStudy(msg):
    try:
        if msg['giftId'] == 85 :
            return True
    except:
        pass
    return False      

def isBeatstorm(msg):
    try:
        if (msg['cmd'] == 'SPECIAL_GIFT') :
            x =  msg['data']['39']
            content = x['content']
            if (type(content) == str and len(content) >0) :
                return True  
    except:
        pass
    return False

msgpool = []
msgmutex = threading.Lock() 


def dealmsg(msg):
    f = False
    f = f or isTv(msg)
    f = f or isStudy(msg)
    
    if f is False:
        return
    
    msgmutex.acquire()
    
    for m in msgpool:
        if (m == msg) :
            break
    else:
        msgpool.append(msg)
        
    msgmutex.release()
        
        
        
        
def dealtv():
    msgmutex.acquire()
    msg = None
    for m in msgpool:
        if isTv(m) :
            msg = m
            break
    if msg is None :
        msgmutex.release()
        return
    
    msgpool.remove(msg)
    msgmutex.release()

    try:
        re = robtv(msg['url'], msg['real_roomid'], msg['tv_id'])
        
        re = json.loads(re)
        if ('code' in re) :
            if re['code'] !=0 :
                for i in range(0,5) :
                    winsound.Beep(600,500)
                    winsound.Beep(300,500)
                    winsound.Beep(900,500)
        
    except Exception as e :
        print('dealtv except', e)


def dealStudy():
    
    pass    
    
def work():
    print("enter rob work")
    while True:
        time.sleep(1)
        try:
            dealStudy()
        except Exception as e :
            print('work except', e)        
        

robthread = threading.Thread(target=work)
robthread.setDaemon(True)
robthread.start()
        
            