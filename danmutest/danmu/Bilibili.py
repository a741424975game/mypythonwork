import socket, json, re, select, time, random
from struct import pack
from struct import unpack
import requests, zlib

from .Abstract import AbstractDanMuClient

class _socket(socket.socket):
    def push(self, data, type = 7):
        data = (pack('>i', len(data) + 16) + b'\x00\x10\x00\x01' +
            pack('>i', type) + pack('>i', 1) + data)
        self.sendall(data)
    def pull(self):
        try: # for socket.settimeout
            return self.recv(9999)
        except Exception as e:
            return ''

class BilibiliDanMuClient(AbstractDanMuClient):
    
 
    def _get_live_status(self):
        #print("sssssss")
        x1 = self.url.split('/')[-1] or self.url.split('/')[-2];
        #print(x1)
        url = ('http://api.live.bilibili.com/room/v1/Room/room_init?id='  + x1)
        #print(url)
        x = requests.get(url).content
        # print (x)
        y = json.loads(x.decode('ascii'))
        #print(y)
        #self.roomId = re.findall(b'WebSocket On Open\. rid\:(\d+)\n', x)[0].decode('ascii')
        self.roomId = y['data']['room_id']
        #print(self.roomId)
        url = 'http://live.bilibili.com/api/player?id=cid:' + str(self.roomId)
        r = requests.get(url)
        
        #print(r.content)
        self.serverUrl = re.findall(b'<server>(.*?)</server>', r.content)[0].decode('ascii')
        self.port = re.findall(b'<dm_port>(.*?)</dm_port>', r.content)[0].decode('ascii')
 
        return True
        return re.findall(b'<state>(.*?)</state>', r.content)[0] == b'LIVE'
    def _prepare_env(self):
        self.cache = b''
        return (self.serverUrl, int(self.port)), {}
    def _init_socket(self, danmu, roomInfo):
        #print('danmu socket init')
        self.danmuSocket = _socket()
        self.danmuSocket.connect(danmu)
        self.danmuSocket.settimeout(3)
        self.danmuSocket.push(data = json.dumps({
            'roomid': int(self.roomId),
            'uid': 82778,
            'protover': 2,
            }, separators=(',', ':')).encode('ascii'))
    def _create_thread_fn(self, roomInfo):
        def keep_alive(self):
            self.danmuSocket.push(b'', 2)
            time.sleep(30)
        def get_danmu(self):
            if not select.select([self.danmuSocket], [], [], 1)[0]: return
            content = self.danmuSocket.pull()
            #print(content)
            #print('\n')
 
            self.cache += content
            
            while (True) :
                if (len(self.cache) <8):
                    break
                l,x = unpack('!ih', self.cache[0:6])
                 
                if (x != 16):
                    print (self.cache)
                    raise Exception('Error danmu head!!!!!!!!!!!!!!!!!!')
                
                if ( len(self.cache) < l):
                    break;
                deals = self.cache[0:l]
                self.cache = self.cache[l:]
                
                self.danmuWaitTime = time.time() + self.maxNoDanMuWait
                
                if (len(deals) < 30):
                    continue
                data = deals[16:]
                #print (data)
                try:
                    if (data[0:1] == b'x') :
                        x = zlib.decompress(data)
                        #print (x)
                        if (len(x) < 20):
                            continue
                        deals = x
                except Exception as e:
                    print(e)
                    
                for msg in re.findall(b'\x00({[^\x00]*})', deals):
                    try:
                        msg = json.loads(msg.decode('utf8', 'ignore'))
                        msg['NickName'] = (msg.get('info', ['','',['', '']])[2][1]
                            or msg.get('data', {}).get('uname', ''))
                        msg['Content']  = msg.get('info', ['', ''])[1]
                        msg['MsgType']  = {'SEND_GIFT': 'gift', 'DANMU_MSG': 'danmu',
                            'WELCOME': 'enter'}.get(msg.get('cmd'), 'other')
                    except Exception as e:
                        print("impossible")
                        print(e)
                        print(msg)
                        pass
                    else:
                        self.msgPipe.append(msg)   
 
            return
 
        return get_danmu, keep_alive # danmu, heart
