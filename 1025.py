import sys

def quicksort(a,start,end):
    #print (start,end)
    #print a
    if start >= end:
        return
    pivot = start
    pivotValue = a[pivot]
    a[pivot],a[end] = a[end],a[pivot]
    storeIndex = start
    for i in xrange(start,end):
        if a[i]<pivotValue:
            a[i],a[storeIndex] = a[storeIndex],a[i]
            storeIndex += 1
    a[storeIndex],a[end] = a[end],a[storeIndex]
    quicksort(a,start,storeIndex)
    quicksort(a,storeIndex+1,end)

def half(x):
    if x%2 == 0:
        return x/2+1
    else:
        return (x+1)/2

input = sys.stdin

s = input.readline().strip()
s = int(s)
nums = input.readline().strip().split(' ')
nums = [int(x) for x in nums]
quicksort(nums,0,len(nums)-1)

mid = (s+1)/2

sum = reduce(lambda x,y:x+y,[half(x) for x in nums][:mid])

print sum



