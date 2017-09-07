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

        if (msg['NickName'] == '十八呀么十八喵') :
            #robgift.sendDanmu(356767, emoji.randEmoji())
            robgift.bbbb()
            pp('[%s] %s' % (msg['NickName'], msg['Content']))
        
 
        
    except Exception as e:
        print('danmu_fn', e)
    
    return
    

@dmc.gift
def gift_fn(msg):
    return
    pp('[%s] sent a gift!' % msg['NickName'])

xxx = None


@dmc.other
def other_fn(msg):
    
    print(msg)
    if robstudy.isStudy(msg):
        robgift.bbbb()
        global xxx
        
        if (xxx is not None) : xxx.stop()
        xxx = DanMuClient(msg['url'])
        xxx.start(blockThread =  False)
        
        @xxx.other
        def new_other_fn(msg):
            print('inner', msg)
        
    
print('4')
dmc.start(blockThread=False)

print('5')
print('test2')


def ttt(msg):
    
    temp = msg
    a = 1
    def xxx():
        print(temp)
        nonlocal a
        a +=1
        print(a)
    return xxx

a1 = ttt(123)
a2 = ttt(321)

a1()
a1()
a2()
a2()
"""
{'cmd': 'RAFFLE_END', 'roomid': 127932, 'data': {'raffleId': 27932, 'type': 'school', 'from': '荣耀神之领域', 'win': {'uname': '鱼渴渴', 'giftName': '自动铅笔盒', 'giftId': 84, 'giftNum': 24}}, 'NickName': '', 'Content': '', 'MsgType': 'other'}

"""


if __name__ == "__main__":
    while True:
        time.sleep(0.1)

