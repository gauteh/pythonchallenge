import urllib.request


u = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d'
# k = 12345
k = 16044 // 2

while True:
  with urllib.request.urlopen (u % k) as resp:
    html = resp.read()
    print (html)

    i = html.rfind (b' ')
    k = int(html[i:]) // 2

    print (k)

    if i < 1:
      break
