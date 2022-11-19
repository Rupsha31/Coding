def productarray(crr,n):
    l=[]
    for i in range (n):
        p=1
        for j in range (n):
            if(i!=j):
                p=p*crr[j]
        l.append(p)
    return l
if __name__ == '__main__' :
    t=int(input())
    while t != 0 :
        n = int(input())
        crr = [int(x) for x in input().strip().split()]
        ans=productarray(crr,n)
        print(*ans)
        t-=1
