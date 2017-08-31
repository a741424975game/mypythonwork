﻿# -*- coding: UTF-8 -*-

import time, sys, os, json
import winsound

import robgift 





from danmu import DanMuClient


import realtest 
 



print(sys.path)

print (os.getcwd())


print('1111')

def pp(msg):
    print(msg.encode(sys.stdin.encoding, 'ignore').
        decode(sys.stdin.encoding))

print('2')
target = 'http://live.bilibili.com/356767'
print(target)
dmc = DanMuClient(target)
if not dmc.isValid(): print('Url not valid')


print('3')



@dmc.danmu
def danmu_fn(msg):
    pp('[%s] %s' % (msg['NickName'], msg['Content']))
    return
    

@dmc.gift
def gift_fn(msg):
    return
    pp('[%s] sent a gift!' % msg['NickName'])

@dmc.other
def other_fn(msg):
    pp('Other message received')
    localtime = time.localtime(time.time())
    ts = time.strftime("%Y %m %d %H:%M:%S", localtime)
    print ('local:', ts)
    print(msg)
    
    if (robgift.isBeatstorm(msg)):
        try:
            robgift.robBeatstorm(msg)
        except:
            print ('rob beatstorm fail')
        return 
    
    if ('tv_id' in msg) :
        winsound.Beep(600,500)
        try:
            re = robgift.robtv(msg['url'], msg['real_roomid'], msg['tv_id'])
            
            re = json.loads(re)
            if ('code' in re) :
                if re['code'] !=0 :
                    for i in range(0,5) :
                        winsound.Beep(600,500)
                        winsound.Beep(300,500)
                        winsound.Beep(900,500)
            
        except Exception as e :
            print('robgift except', e)
            
        return
    if (robgift.isStudy(msg)) : 
        try:
            robgift.robstudy(msg['url'], msg['real_roomid'])
        except:
            print('rob study fail!!')
        return
        
print('4')
dmc.start(blockThread=False)


 

print('5')

while True:
    time.sleep(0.1)

