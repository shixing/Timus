import sys

n = int(sys.stdin.readline().strip())

temp = 0
count = 0
line = sys.stdin.readline()
na = ord(line[0])-48
nb = ord(line[2])-48
temp = (na+nb) % 10

for line in sys.stdin:
    #print line
    na = ord(line[0])-48
    nb = ord(line[2])-48
    if na+nb<9:
        sys.stdout.write(str(temp))
        for i in xrange(count):
            sys.stdout.write('9')
        count = 0
        temp = na+nb
    elif na+nb==9:
        count += 1
    else:
        sys.stdout.write(str(temp+1))
        for i in xrange(count):
            sys.stdout.write('0')
        count = 0
        temp = na+nb-10

sys.stdout.write(str(temp))
for i in xrange(count):
    sys.stdout.write('9')
print
