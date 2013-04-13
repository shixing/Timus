import sys
import math

line = sys.stdin.readline().split()
line = [float(x) for x in line]
a = line[0]
r = line[1]

if r >= math.sqrt(2) * a / 2:
    print '%.3f' % (a*a)
elif r< a/2:
    print '%.3f' % (math.pi*r*r)
else:
    area = math.pi * r*r
    shan = math.acos(a/2/r)*2/(math.pi*2)*area
    sanjiao = math.sqrt(r*r-(a/2)*(a/2))*a/2
    print '%.3f' % (area-4*(shan-sanjiao))
