# -*- coding: UTF-8 -*-
import threading, re, requests, time, json
import robgift

from danmu import DanMuClient

"""
Other message received
local: 2017 09 04 15:25:23
{'cmd': 'SYS_GIFT', 'msg': '阿梓家的猛男:? 在直播间 :?80397:? 使用了 20 倍节奏风暴，大家快去跟风领取奖励吧！',
 'tips': '【阿梓家的猛男】在直播间【80397】使用了 20 倍节奏风暴，大家快去跟风领取奖励吧！', 
 'giftId': 39, 'msgTips': 1, 'url': 'http://live.bilibili.com/80397', 
 'roomid': 80397, 'rnd': 1504509162, 'NickName': '', 'Content': '', 'MsgType': 'other'}
 
 
 

{"cmd": "SPECIAL_GIFT", "data": {"39": {"id": "114259", "num": 100, "time": 90,
"content": "刚刚回帝都了，庆祝下", "hadJoin": 0, "action": "start"}}, "NickName"
: "", "Content": "", "MsgType": "other"}
Other message received
local: 2017 08 30 15:15:22
{"cmd": "SPECIAL_GIFT", "data": {"39": {"action": "end"}}, "NickName": "", "Cont
ent": "", "MsgType": "other"}
 
Other message end


{"code":0,"message":"OK","msg":"OK","data":
{"cmd":"SPECIAL_TIPS","tips":
{"gift_id":39,"title":"\u8282\u594f\u98ce\u66b4",
"content":"<p>\u4f60\u662f\u524d 2000 \u4f4d\u8ddf\u98ce\u5927\u5e08<br \/>\u606d\u559c\u4f60\u83b7\u5f97\u4e00\u4e2a\u4ebf\u5706(7\u5929\u6709\u6548\u671f)<\/p>",
"mobile_content":"\u4f60\u662f\u524d 2000 \u4f4d\u8ddf\u98ce\u5927\u5e08",
"gift_img":"http:\/\/static.hdslb.com\/live-static\/live-room\/images\/gift-section\/gift-6.png?2017011901",
"gift_num":1,"gift_name":"\u4ebf\u5706"}}}


{"code":0,"message":"OK","msg":"OK",
    "data":
    {"gift39":
    {"id":"117336","num":4000,"time":49,"content":"\u6253call\u6253call","hadJoin":1}}}

"""

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
def isGlobalBeatstrom(msg):
    try:
        if (msg['cmd'] == 'SYS_GIFT') and msg['giftId'] == 39:
            msg['url']
            return True  
    except:
        pass
    return False   

def robBeatstorm(msg, realroomid = 356767):
   
    print('rob local beat storm')
    try:
        realroomid = int(realroomid)
        x =  msg['data']['39']
        content = x['content']
    except:
        print ("rob beatstorm error")
        return

    robgift.sendDanmu(realroomid, content)
    
    return

def robglobalstormwork(msg):
    url = msg['url']
    print(url)
    dmc = DanMuClient(url)
    if not dmc.isValid(): 
        print('Url not valid')
        return
    else : 
        print('url ok')
    
    realroomId = re.findall(b'var ROOMID = (\d+);', requests.get(url).content)[0].decode('ascii')
    if (realroomId == 356767) :
        print('356767   same  ')
        return
    
    danmu_count = {}
    print(' robglobalstormwork realroomId ', realroomId)
    @dmc.danmu
    def danmu_fn(msg, realroomid = realroomId):
        try:
            m = msg['Content']
            
            if (m not in danmu_count):
                danmu_count [m] = 1;
            else :
                danmu_count[ m] +=1
            
            #print(danmu_count)    
            
            if danmu_count[m] >10 :
                print ('send duplicate 25')
                for i in range(4):
                    re = robgift.sendDanmu(realroomid, m)
                    if (re.find('"msg":""') != -1): break
                    time.sleep(4.0)
                dmc.stop()
                danmu_count.clear()
        except Exception as e:
            print(e)
        
    @dmc.other
    def other_fn(msg, realroomid = realroomId):
        print('storm other fn', msg)
        if not isBeatstorm(msg) : return
        
        robBeatstorm(msg, realroomid)
        time.sleep(4.0)
        robBeatstorm(msg, realroomid)
        time.sleep(4.0)
        robBeatstorm(msg, realroomid)
        time.sleep(4.0)
        robBeatstorm(msg, realroomid)
        time.sleep(4.0)
        robBeatstorm(msg, realroomid)
        
        print('rob global beat storm  end')
        
        pass
    
    dmc.start(blockThread=False)
    time.sleep(100)
    dmc.stop()
    print('robglobalstormwork  end')
    
def robglobalstormwork2(msg):
    
    print('try  new robglobalstormwork2')
    
    url = msg['url']
    print(url)
    
    realroomId = re.findall(b'var ROOMID = (\d+);', requests.get(url).content)[0].decode('ascii')
    if (realroomId == 356767) :
        print('356767   same  ')
        return
    try:
        u11 = "http://api.live.bilibili.com/SpecialGift/room/%s" % (realroomId)
        print(u11)
        xxx = requests.get(u11).content[0].decode('utf-8')
        print(xxx)
        jo = json.loads(xxx)
        xxx = jo['data']['gift39']
        if xxx['hadJoin'] == 1: return True
        
        m = xxx['content']
        print(m)
        m = m.decode('utf-8')
        print(m)
        
        return False
        
        r = robgift.sendDanmu(realroomId, m)
        
        print(r)
        jo = json.loads(r)
        
        return isBeatstorm(jo)
        
        
    except Exception as e:
        print(e)
    
    return False
    
def robglobaltest(msg):
    try:
        if (robglobalstormwork2(msg)): return
    except Exception as e:
        print('robglobaltest11111',e)
    try:
        robglobalstormwork(msg)
    except Exception as e:
        robgift.bbbb()
        robgift.bbbb()
        print('robglobaltest22222',e)
     
def robGlobalstorm(msg):
    print('rob global beat storm begin')
    t = threading.Thread(target = robglobaltest, args = (msg,));
    t.setDaemon(True)
    t.start()
    
    pass

def robBeatstormWork(msg):
    try:
        if isBeatstorm(msg):
            robBeatstorm(msg)
            return
    except Exception as e:
        print ('rob local beat storm fail', e)
    
    try:
        if (isGlobalBeatstrom(msg)):
            robgift.bbbb()
            robGlobalstorm(msg)
            return
    except Exception as e:
        print ('rob glabol beat storm fail', e)
        
        
if __name__ == "__main__":
    
    d = {}
    d[1] = 1
    d[1] +=2
    print(d)
    
    test = """
    {"cmd": "SYS_GIFT", "msg": "阿梓家的猛男:? 在直播间 :?80397:? 使用了 20 倍节奏风暴，大家快去跟风领取奖励吧！",
 "tips": "【阿梓家的猛男】在直播间【80397】使用了 20 倍节奏风暴，大家快去跟风领取奖励吧！", 
 "giftId": 39, "msgTips": 1, "url": "http://live.bilibili.com/82789", 
 "roomid": 80397, "rnd": 1504509162, "NickName": "", "Content": "", "MsgType": "other"}
 """
    m = json.loads(test)
    print(m)
    robGlobalstorm(m)
    while True:
        time.sleep(0.1)