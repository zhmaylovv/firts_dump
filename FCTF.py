import requests
'''
session = requests.session()
session.headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Trident/4.0;)'
rs = session.request('get', "https://sheep.ilovefrontend.ru/browser.html")
print(rs)
'''

import base64
d = base64.b64decode('bXltZWdhc3VwZXJwYXNz')
print(d) #b'35.141533,-90.052695'


#print(bytes.fromhex('MzUuMTQxNTMzLC05MC4wNTI2OTU=').decode('utf-8'))

'''


a = ''
s = 'MzUuMTQxNTMzLC05MC4wNTI2OTU='
c = 0
for i in s:
    if i.isupper():
        s = ord(i)
        a+=chr(s+1)

    elif i.islower():
        s = ord(i)
        a += chr(s - 1)

res = 'nyvtnsrwosnymb14nb5vosj1psv< _ NyVtNSRwOSNyMB14NB5vOSJ1PSV<'
print(a)
'''

'''
#part of saturn solution + js + hz
session = requests.session()
session.headers['User-Agent']= '_flock'
rs = session.request('post', "https://fctf3-saturn.now.sh/xhr" )
'''
'''

#Neptune solution
session = requests.session()
session.headers['User-Agent']= 'Neptune'
session.headers['referer']= 'Boris'
rs = session.request('get', "https://fctf3-neptune.now.sh")

'''




#neptune
