def Palin(arr,n):
    j=0
    for i in arr:
        s=0
        m=i
        while m > 0:
            s=s*10
            s=s+m%10
            m=int(m/10)
        if(s != i):
            return 0
        j+=1
    if(j == n):
        return 1
    
if __name__ =='__main__' :
    t=int(input())
    while t != 0:
        n=int(input())
        brr= [int(x) for x in input().strip().split()]
        if Palin(brr,n):
            print(1)
        else:
            print(0)

