# -*- coding: UTF-8 -*-
import random, time, urllib, threading, json 
import robgift
import bilibilicookie


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


def robBeatstorm(msg):
#url = ('http://live.bilibili.com/'
#+ self.url.split('/')[-1] or self.url.split('/')[-2])
#self.roomId = re.findall(b'var ROOMID = (\d+);', requests.get(url).content)[0].decode('ascii')
    print('rob beat storm')
    try:
        x =  msg['data']['39']
        content = x['content']
    except:
        print ("rob beatstorm error")
        return

    robgift.sendDanmu(356767, content)
    
    return



def robBeatstormWork(msg):
    try:
        if not isBeatstorm(msg): return
        robBeatstorm(msg)
    except Exception as e:
        print ('rob beat storm fail', e)
    
    