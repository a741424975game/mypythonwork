# -*- coding: UTF-8 -*-
import random, time, urllib, threading, json, requests, gzip
import robgift
import bilibilicookie

    
studyHistory = []
studyCheck = []
def isStudy(msg):
    try:
        if msg['giftId'] == 85 :
            return True
    except:
        pass
    return False      

def robstudy(roomurl, realroomid,   test = False):
    print('rob study')
    

    
    delay =  random.randint(2000, 4000)
    if  test is False :
        time.sleep( delay/ 1000.0)
     
    realroomid = str(realroomid)
    
    data = []
    try:
        u1 = "http://api.live.bilibili.com/activity/v1/SchoolOpen/check?roomid=" +  (realroomid)
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
            url = "http://api.live.bilibili.com/activity/v1/SchoolOpen/join" 
            raffleId = target['raffleId']
             
            if (raffleId in studyHistory):
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
                "Cookie":bilibilicookie.nowcookie,
                "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Host":"api.live.bilibili.com",
                "Origin":"http://live.bilibili.com",
                "Referer": roomurl,
                 
                "User-Agent":bilibilicookie.nowagent,
                        
                }
            
            print('try rob study')
            print(postdata)
            
            req = urllib.request.Request(url,postdata,header)
            
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
        time.sleep(0.5)
        robgift.sendDanmu(realroomid, '(-_-)')        
    
    return True


def checkstudyresult(roomurl, realroomid, raffleid):
    realroomid = int(realroomid)
    raffleid = int(raffleid)

    url = "http://api.live.bilibili.com/activity/v1/SchoolOpen/notice?roomid=%d&raffleId=%d" % (  realroomid, raffleid)
    
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

def robstudywork(msg):
    try:
        re = robstudy(msg['url'], msg['real_roomid'])
        re = json.loads(re)
        if ('code' in re) :
            if re['code'] !=0 :
                robgift.bbbb()
                return
    except Exception as e :
        print('robgift except', e)
        robgift.bbbb()
        return
        
    print ('rob study ok')
    time.sleep(80)
    try:
        checkstudyresult(msg['url'],  msg['tv_id'])
    except Exception as e :
        print(e)
        
        
def robstudythread(msg):
    if not isStudy(msg) : return
    t = threading.Thread(target= robstudywork, args=(msg,))
    t.setDaemon(True)
    t.start()
    
def studycheck():
    pass


t = threading.Thread(target= studycheck)
t.setDaemon(True)
t.start()

    
if __name__ == '__main__':    
    
    print ('dfasdf')
    robstudythread(1)
    
    while True:
        time.sleep(1)