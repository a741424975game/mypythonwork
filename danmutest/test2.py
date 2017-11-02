# -*- coding: UTF-8 -*-

import time, sys, os 
 
 


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

 
        pp('[%s] %s' % (msg['NickName'], msg['Content']))
        
 
        
    except Exception as e:
        print('danmu_fn', e)
    
    return
    

@dmc.gift
def gift_fn(msg):
     
    pp('[%s] sent a gift!' % msg['NickName'])

xxx = None


@dmc.other
def other_fn(msg):
    
    print(msg)
     
        
    
print('4')
dmc.start(blockThread=False)

 

 


if __name__ == "__main__":
    while True:
        time.sleep(0.1)

