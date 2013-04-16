import sys

input = sys.stdin

line =input.readline()

ll=line.split()

n = int(ll[0])
k = len(ll[1])

sum = 1
i=0
while True:
   e = n-k*i
   i+=1
   if e<=0:
       break
   sum*=e
print sum   
