import sys

n = int(sys.stdin.readline().strip())
db = []
for i in xrange(n):
    nn = int(sys.stdin.readline().strip())
    db.append(nn)
sys.stdin.readline()
nq = int(sys.stdin.readline().strip())
qs = []
for i in xrange(nq):
    nn = int(sys.stdin.readline().strip())
    qs.append(nn-1)

def quicksort(array,start,end):

    if start>=end-1:
        return
    pivotValue = array[start]
    storedIndex = start
    array[start],array[end-1] = array[end-1],array[start]
    for i in xrange(start,end-1):
        if array[i]<pivotValue:
            array[storedIndex],array[i]=array[i],array[storedIndex]
            storedIndex+=1
    array[end-1],array[storedIndex]=array[storedIndex],array[end-1]
    quicksort(array,start,storedIndex)
    quicksort(array,storedIndex+1,end)

quicksort(db,0,len(db))

for q in qs:
    print db[q]
