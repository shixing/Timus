import sys
# this method failed, because it's o(n^2)

def under(xstop,value,temp_xstop,temp_value,x,i,preN):
    while True:
        if i==len(xstop)-1:
            break
        if xstop[i+1] > x:
            break
        i+=1
        temp_xstop.append(xstop[i])
        temp_value.append(value[i]+preN)
    return i


n = int(sys.stdin.readline().strip())
points = []
for line in sys.stdin:
    ll = line.split()
    points.append((int(ll[0]),int(ll[1])))

levels = [0]*n

xstop = []
value = []

temp_xstop = [-1]
temp_value = [0]

old_y = -1
preN = 0
ixstop = 0
for (x,y) in points:
    if y != old_y:
        old_y = y
        for j in xrange(len(xstop)):
            if xstop[j] > temp_xstop[-1]:
                temp_xstop.append(xstop[j])
                temp_value.append(value[j]+preN)
        #print temp_xstop
        #print temp_value

        xstop = temp_xstop
        value = temp_value
        temp_xstop = [-1]
        temp_value = [0]
        preN = 0
        ixstop = 0 
        
    ixstop = under(xstop,value,temp_xstop,temp_value,x,ixstop,preN)
    level = preN + value[ixstop]

    preN += 1
    if temp_xstop[-1] != x:
        temp_xstop.append(x)
        temp_value.append(level+1)
    else:
        temp_value[-1]= level+1
    levels[level] +=1

for x in levels:
    print x
