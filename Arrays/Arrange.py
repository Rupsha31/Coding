def Rearrange( a, n):
    l=[]
    k=[]
    # Your code goes here
    for i in a:
        if i < 0:
            l.append(i)
        else:
            k.append(i)
    j=len(l)
    m=len(k)
    s=0
    for i in range(j):
        a[s]=l[i]
        s=s+1
    for i in range(m):
        a[s]=k[i]
        s+=1
if __name__ == '__main__':
    tc=int(input())
    while tc > 0:
        n=int(input())
        a = [int(y) for y in input().strip().split()]
        Rearrange(a,n)
        print(*a)
        tc-=1