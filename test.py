import sys
a = 10
for i in range(a):
    for j in range(a-i):
        print ('_', end='')
    for k in range(i):
        print ('*',end='')
    print()
