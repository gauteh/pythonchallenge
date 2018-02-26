import urllib.request


u = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%.1f'
# k = 12345
k = 16044 / 2

while True:
  print (u % k)
  with urllib.request.urlopen (u % k) as resp:
    html = resp.read()
    print (html)

    i = html.rfind (b' ')
    k = float(html[i:]) 

    print (k)

