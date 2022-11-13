def firstandlast(arr,n,x):
    l=[]
    k=[]
    for i in range(n):
        if(arr[i] == x):
            l.append(i)
    s=len(l)
    k.append(l[0])
    k.append(l[s-1])
    return k
if __name__== '__main__':
    t= int(input())
    while t != 0:
        n=int(input())
        x=int(input())
        arr=[int(k) for k in input().strip().split()]
        ans=firstandlast(arr,n,x)
        print(*ans)
        t-=1
