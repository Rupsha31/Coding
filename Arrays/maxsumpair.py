def maxSumPairWithDifferenceLessThanK(arr, N, K): 
    # Your code goes here 
    arr.sort(reverse=True)
    i=0
    c=0
    while i<N-1:
        if (arr[i]-arr[i+1])<K:
            c+=arr[i]+arr[i+1]
            i+=2
        else:
            i+=1
    return c
if __name__ == '__main__':
    tc=int(input())
    while tc >0:
        n=int(input())
        a=[int(x) for x in input().strip().split()]
        k=int(input())
        print(maxSumPairWithDifferenceLessThanK(a,n,k))
        tc-=1