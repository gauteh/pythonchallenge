
import pickle

with open ('5.in', 'rb') as fd:
  s = pickle.load (fd)
# print (s)

for t in s:
  for tt in t:
    n = tt[1]
    c = tt[0]
    for i in range(n):
      print (c, end = '')
  print()

