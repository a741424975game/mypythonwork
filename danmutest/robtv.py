# -*- coding: UTF-8 -*-
import random, time, urllib, threading, json, requests 
import robgift
import bilibilicookie

def isTv(msg):
    try:
        if ('tv_id' in msg):
            return True
    except:
        pass
    
    return False

tvset1 = set()
tvset2 = set()

def checkTV(realroomid, tv_id):
    try:
        tv_id = int(tv_id)
        tvset1.add(tv_id)
        url = "https://api.live.bilibili.com/gift/v2/smalltv/check?roomid=" + str(realroomid);
        x0 = requests.get(url).content
 
        x = x0.decode('utf-8')
 
        jo = json.loads(x)
        """
            {"code":0,"msg":"OK","message":"OK","data":[{"raffleId":28872,"type":"small_tv","from":"","from_user":null,"time":0,"status":0}]}

        """
        a = jo["data"]
        if (not isinstance(a, list)):
            return True;
        same= False
        for x in a:
            rid =int(x["raffleId"])
            tvset2.add(rid)
            if ( rid == tv_id): same = True
            pass
        d = tvset2.difference(tvset1)
        if (len(d) >0) : 
            print("!!!!!!!! mystery tv id",d)
        
        if same: return True
        print(x0)
        return False
    except Exception as e:
        print('checkTV', e);
        
    return True

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
        print(robgift.printtime(), file = fo)
        print(url, file = fo)
        print(re, file = fo)
        fo.close()
    except Exception as e:
        print('save result file', e)

def robtvwork(msg):
    try:
        x = checkTV(msg['real_roomid'], msg['tv_id'])
        if not x:
            print("missing tv id");
            return
        robgift.moniterDanmu(msg['url'], 400)
        re = robtv(msg['url'], msg['real_roomid'], msg['tv_id'])
        re = json.loads(re)
        if ('code' in re) :
            if re['code'] !=0 :
                robgift.bbbb()
                return
    except Exception as e :
        print('robtv except', e)
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
    sss = {1,2,3,5,6,6}
    print(len(sss))
    print ('robtv main')
    x = checkTV(24541, 28872)
    print(x)
    exit()
    
    robtvthread(1)
    
    while True:
        time.sleep(1)

    

