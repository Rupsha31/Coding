def Rearrange( a, n):
        p=[]
        n=[]
        for i in range(len(a)):
            if a[i]>=0:
                p.append(a[i])
            else:
                n.append(a[i])
        j=0
        k=0
        l=0
        p_len=len(p)
        n_len=len(n)
        arr_len=len(a)
        while j<arr_len:
            if k< p_len and j<arr_len+1 :
                a[j]=p[k]
                k=k+1
                j=j+1
            if l<n_len and j<arr_len+1:
                a[j]=n[l]
                l=l+1
                j=j+1
if __name__ == '__main__':
    tc=int(input())
    while tc > 0:
        n=int(input())
        a = [int(y) for y in input().strip().split()]
        Rearrange(a,n)
        print(*a)
        tc-=1