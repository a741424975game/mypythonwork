# -*- coding: UTF-8 -*-

import time, random, json, urllib

import robgift

if False:
    ssss = """
{"cmd": "SPECIAL_GIFT", "data": {"39": {"id": "114259", "num": 100, "time": 90,
"content": "刚刚回帝都了，庆祝下", "hadJoin": 0, "action": "start"}}, "NickName"
: "", "Content": "", "MsgType": "other"}
    """
    bs = json.loads ( ssss )
    print(bs)
    ffff = robgift.isBeatstorm(bs)
    print(ffff)
    
    robgift.sendDanmu(82789, "啊asd", test = True)
    
    re1 = robgift.robtv("bilibili.tv", 435345, '345456', True)
    
    print(re1)
    try:
        js1 = json.loads(re1)
        print(js1)
    except:
        pass
    
    
    ls = """
    {"code":0,"msg":"OK","data":{"id":25019,"dtime":177,"status":1}}
    """
    re = json.loads(ls)
    
    print(ls)
    
    print(re)
    print(re.keys())
    
    print ('random',  random.randint(1000,  3000))
    print (123123/ 20.0)
     
    print(int(time.time()))
    print (int ('123123'))
    
    
    localtime = time.localtime(time.time())
    ts = time.strftime("%Y %m %d %H:%M:%S", localtime)
    print ('local:', ts)
    
    fff = {'Name': 'Zara', 'Age': 7};
    
    try:
        print(fff['sdf'])
    except:
        print ('except')
    
    
    if 'Name' in fff:
        print('if Name in fff:')
        pass
    
    
    def maker(N):
            def action(X):
                return X**N
            return action
    f = maker(2)
    print(f(2))
    
    f1 = maker(3)
    print(f1(2))
    print(f(2))
    
    
    
    def funA(a):
        print ('AAA')
        print(a)
        return 'testa'
    
    def funB(b):
        print ('funB')
        print(b)
        return 'testb'
    
    @funA
    @funB
    def funC1():
        print ('funC1')
        
        
    print ('-------------')
    
    print(funC1)
    funC1 = funA
    
    print ('-------------')
    
    class test1:
        def __init__(self):
            print("test1 init")
     
        def __del__(self):
            print("test1 del")
     
        
    
    def testaa():
        
        xxx = test1()
        
    
    testaa()