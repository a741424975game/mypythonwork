# -*- coding: UTF-8 -*-

import time, sys, os 
 

import robgift 
import robtv
import robstudy
import robbeatstorm


from danmu import DanMuClient
 

 

 


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
    try:

        if (msg['NickName'] == '十八にゃ') :
            #robgift.sendDanmu(356767, emoji.randEmoji())
            robgift.bbbb()
            print(msg)
            pp('[%s] %s' % (msg['NickName'], msg['Content']))
        
        fo = open('danmu.txt', 'a',  encoding ='utf-8')
        print(msg, file = fo)
        fo.close()
        
    except Exception as e:
        print('danmu_fn', e)
    
    return
    

@dmc.gift
def gift_fn(msg):
    return
    pp('[%s] sent a gift!' % msg['NickName'])

@dmc.other
def other_fn(msg):
    
    print('Other message received')
    try:
        localtime = time.localtime(time.time())
        ts = time.strftime("%Y %m %d %H:%M:%S", localtime)
        print ('local:', ts)
        print(msg)
    except Exception as e:
        print('other_fn', e)
        
    try:
        fo = open('other.txt', 'a', encoding = 'utf-8')
        print(ts, file = fo)
        print(msg, file = fo)
        fo.close()
    except Exception as e:
        print('save file', e)
    
    
    robbeatstorm.robBeatstormWork(msg)
    robtv.robtvthread(msg)
    
    #robstudy.robstudythread(msg)
    
    print('Other message end')    
    
print('4')
dmc.start(blockThread=False)

print('5')




if __name__ == "__main__":
    while True:
        time.sleep(0.1)

