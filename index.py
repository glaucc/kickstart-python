import sys
sys.stdin = open('input.txt', "r")

t = int(input())
total = 0
tc = 0
while t>0:
    unit = 0
    l,n = input().split()
    l = int(l)
    n = int(n)
    for q in range(n):
        d,c = input().split()
        d = int(d)        
        if c == "C":
            total += d
        elif c == "A":
            total -= d
    unit += total//l
    tc += 1
    print('Case #'+str(tc)+': '+str(unit))
    total = 0
    unit = 0
    t -= 1