#! /usr/bin/env python

s = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

# from string import maketrans

k = [ 'k', 'o', 'e']
v = [ 'm', 'q', 'g']

for kk,vv in zip(k,v):
  print (ord(vv) - ord(kk))

ki = ''.join([ chr(ord('a') + c) for c in range(26) ])
vi = ''.join([ chr(ord('a') + ((c + 2) % 26)) for c in range(26) ])

T = str.maketrans (ki, vi)
o = s.translate (T)

print (o)

url = 'http://www.pythonchallenge.com/pc/def/map.html'

u = url.translate (T)
print (u)


