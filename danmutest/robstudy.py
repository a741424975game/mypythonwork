# -*- coding: UTF-8 -*-
import random, time, urllib, threading, json, requests, gzip
import robgift
import bilibilicookie

    
studyHistory = []
studyCheck = []
studymutex = threading.Lock() 
def isStudy(msg):
    try:
        if int(msg['giftId']) == 103 :
            return True
    except:
        pass
    return False      

def robstudy(roomurl, realroomid,   test = False):
    
    realroomid = str(realroomid)
    print('rob study')
    delay =  random.randint(2000, 4000)
    time.sleep( delay * 2/ 1000.0)
     
    #robgift.sendDanmu(realroomid, '(-_-)' )
    
    time.sleep( delay  / 1000.0)
    data = []
    try:
        u1 = "https://api.live.bilibili.com/activity/v1/Raffle/check?roomid=" +  (realroomid)
        print(u1)
        re0 = requests.get(u1).content
        print(re0)
        re1 = re0.decode('utf-8')
        x = json.loads(re1)
        data = x['data']
    except Exception as e:
        print('get study list fail ')
        print(e)
        print (re1)
        return False
    print(data)
    
    if (type(data) != list):
        return False
    if (len(data) ==0) :
        print('zero list')
        return 0
    acc = 0
    for target in data:
        try:
            #{"code":0,"msg":"success","message":"success",
            #"data":[{"raffleId":"27279","type":"school","from":"黑丝细腿","time":38,"status":1}]}
            url = "https://api.live.bilibili.com/activity/v1/Raffle/join?roomid="  + str(realroomid) + "&raffleId=" + str(target['raffleId'])
            raffleId = int(target['raffleId'])
             
            if (raffleId in studyHistory):
                print ('already inside')
                continue
 
            
            header={
                "Accept":"application/json, text/javascript, */*; q=0.01",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.8",
                "Connection":"keep-alive",
                "Cookie":bilibilicookie.nowcookie,
                "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Host":"api.live.bilibili.com",
                "Origin":"http://live.bilibili.com",
                "Referer": roomurl,
                 
                "User-Agent":bilibilicookie.nowagent,
                        
                }
            
            print('try rob study')
 
            
            req = urllib.request.Request(url,None,header)
            
            r=urllib.request.urlopen(req)
            r1 = r.read();
            try:
                r2 = r1.decode('utf-8')
                r3 = r2
            except:
                r2 = gzip.decompress(r1)
                r3 = r2.decode('utf-8')
            
            try:
                jo = json.loads(r3)
                if (jo['code'] !=0) :
                    robgift.bbbb()
                    print(r1)
                    print(r3) 
                else:
                    print ('rob study ok')
                    studyHistory.append(raffleId)
                    acc +=1
                    
                    studymutex.acquire()
                    studyCheck.append( (roomurl, realroomid, raffleId, time.time()))
                    studymutex.release()
                    
            except Exception as e:
                print(e)
                print(r1)
                print(r3)
                robgift.bbbb() 
            
            time.sleep( 0.1)
            
        except Exception as e:
            print("fail rob study one")
            print (e)
    
    if (acc>0) :
        time.sleep(delay/ 1000.0)
        #robgift.sendDanmu(realroomid, '(;-_-)')        
    
    return True


def checkstudyresult(roomurl, realroomid, raffleid):
    realroomid = int(realroomid)
    raffleid = int(raffleid)

    url = "https://api.live.bilibili.com/activity/v1/Raffle/notice?roomid=%d&raffleId=%d" % (  realroomid, raffleid)
    
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
    re = (r.read().decode('utf-8'))
    print(re)
    
    try:
        fo = open('result.txt', 'a', encoding = 'utf-8')
        print(robgift.printtime(), file = fo)
        print(url, file = fo)
        print(re, file = fo)
        fo.close()
    except Exception as e:
        print('save result file', e)
    

def robstudywork(msg):
    try:
        robgift.moniterDanmu(msg['url'])
        robstudy(msg['url'], msg['real_roomid'])
        print ('rob study finished')
    except Exception as e :
        print('rob study work except', e)
        robgift.bbbb()
        return
        
    
 
        
        
def robstudythread(msg):
    if not isStudy(msg) : return
    t = threading.Thread(target= robstudywork, args=(msg,))
    t.setDaemon(True)
    t.start()
    
def studycheckwork():
    print('start study check work')
    while True:
        time.sleep(2)
        if not studymutex.acquire(1000): continue
        try:
            now = time.time()
            target = None
            for t in studyCheck :
                ts = t[3]
                 
                if (ts + 120   <= now) : 
                    target = t 
                    break
            if (target is not None):
                studyCheck.remove(target)
        except Exception as e:
            print('studycheck 1',e) 
        studymutex.release()
        
        if (target is None): continue
        
        try:
            checkstudyresult(target[0], target[1], target[2])
        except Exception as e:
            print('studycheck 2', e)
        


t = threading.Thread(target= studycheckwork)
t.setDaemon(True)
t.start()

    
if __name__ == '__main__':    
    
    print ('dfasdf')
    robstudythread(1)
    
    while True:
        time.sleep(1)