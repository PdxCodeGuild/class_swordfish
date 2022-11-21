import urllib.request

fp = urllib.request.urlopen("http://www.python.org")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

mystr_clean = ''
for x in mystr:
    recording = True
    if x == '<':
        recording = False
        
    if recording == True:
            mystr_clean += x    

    if x == '>':
        recording = True



print(mystr_clean)