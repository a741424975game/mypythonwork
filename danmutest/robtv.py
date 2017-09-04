# -*- coding: UTF-8 -*-
import random, time, urllib, threading, json 
import robgift
import bilibilicookie

def isTv(msg):
    try:
        if ('tv_id' in msg):
            return True
    except:
        pass
    
    return False

def robtv(roomurl, realroomid, tvid, test = False):
    print('try rob tv')
    delay =  random.randint(3000, 5000)
    print('delay', delay)
    time.sleep( delay * 2/ 1000.0)
    robgift.sendDanmu(realroomid, 'bilibili-乾杯~')      
    
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
        "Cookie": bilibilicookie.nowcookie,
        
        "Host":"api.live.bilibili.com",
        "Origin":"http://live.bilibili.com",
        "Referer": roomurl,
         
        "User-Agent":bilibilicookie.nowagent,
                
        }
    
    print(url)
    #print(header)
    
    req = urllib.request.Request(url,None,header)
 
        
    if test:
        return ""
    
    r=urllib.request.urlopen(req)
    re = (r.read().decode('utf-8'))
    print(re)
    
    time.sleep( delay/ 1000.0)
    
    robgift.sendDanmu(realroomid, 'bilibili--乾杯~~')      
    
    return re

def checktvresult(roomurl, tvid):
    tvid = int(tvid)
    timestamp = int( time.time() * 1000)  
    url = "http://api.live.bilibili.com/SmallTV/getReward?id=%d&_=%d" % (  tvid, timestamp)
    
    #postdata=urllib.parse.urlencode({        "JobName":"测试工程师",        }).encode('utf-8')
    
    header={
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection":"keep-alive",
        "Cookie": bilibilicookie.nowcookie,
        
        "Host":"api.live.bilibili.com",
        "Origin":"http://live.bilibili.com",
        "Referer": roomurl,
         
        "User-Agent":bilibilicookie.nowagent,
                
        }
    
    print(url) 
    
    req = urllib.request.Request(url,None,header)
 
    
    r=urllib.request.urlopen(req)
    print('check tv result', roomurl, tvid)
    re0 = r.read()
    print(re0)
    
    re = (re0.decode('utf-8'))
    print(re)
    
    try:
        fo = open('result.txt', 'a', encoding = 'utf-8')
        print(url, file = fo)
        print(re, file = fo)
        fo.close()
    except Exception as e:
        print('save result file', e)

def robtvwork(msg):
    try:
        re = robtv(msg['url'], msg['real_roomid'], msg['tv_id'])
        re = json.loads(re)
        if ('code' in re) :
            if re['code'] !=0 :
                robgift.bbbb()
                return
    except Exception as e :
        print('robgift except', e)
        robgift.bbbb()
        return
        
    print ('rob tv ok')
    time.sleep(330)
    try:
        checktvresult(msg['url'],  msg['tv_id'])
    except Exception as e :
        print(e)
        
        
def robtvthread(msg):
    if not isTv(msg) : return
    t = threading.Thread(target= robtvwork, args=(msg,))
    t.setDaemon(True)
    t.start()
    
    
if __name__ == '__main__':    
    
    print ('dfasdf')
    robtvthread(1)
    
    while True:
        time.sleep(1)

    

