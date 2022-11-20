def minSubset(A,N):
    A.sort(reverse=True)
    s=0
    k=0
    j=1
    for i in range(N):
        s=s+A[i]
    for i in range(N):
        k+=A[i]
        if(k>s-k):
            return j
        j+=1
if __name__ == '__main__':
    t=int(input())
    while t >0:
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        print(minSubset(arr,n))
        t-=1