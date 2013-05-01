import sys

line = sys.stdin.read()
ll = line.split()
p = ll[0].strip()
q = ll[1].strip()

p = float(p)/100.0
q = float(q)/100.0

i=1

while True:
    n1 = i/(p+0.0000000000001)
    n2 = i/(q-0.0000000000001)
    if int(n1) != int(n2):
        print int(n2)+1
        break
    i+=1

'''
while True:
    a1 = i*p+0.0000000000001
    a2 = i*q-0.0000000000001
    if int(a1) != int(a2):
        print i
        break
    i+=1

'''
'''
while True:
    n1 = i/p
    n2 = i/q
    #print n1,n2
    if int(n2) == n2:
        l = int(n2)+1
        if i*1.0/l> p :
            print l
            break
    elif int(n1)!=int(n2):
        l = int(n2)+1
        if i*1.0/l> p :
            print l
            break
    i+=1
'''
