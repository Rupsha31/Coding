def maximizeSum(a, n, k):
    # Your code goes here
    a.sort()
    i = 0
    j = 0
    while(i<k and a[j]<0 and j<n-1):
        a[j] = abs(a[j])
        j+=1
        i+=1
    while(i<k):
        a[j] = abs(a[j])
        i+=1
    return sum(a)
if __name__ == '__main__':
    tc=int(input())
    while tc >0:
        n=int(input())
        a=[int(x) for x in input().strip().split()]
        k=int(input())
        print(maximizeSum(a,n,k))
        tc-=1

