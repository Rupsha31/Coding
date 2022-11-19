def findMinSum(A,B,N):
        A.sort()
        B.sort()
        sum=0
        for i in range(N):
            sum=sum+ abs(A[i]-B[i])
        return sum
if __name__ == '__main__':
    t=int(input())
    while t >0:
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        brr=[int(x) for x in input().strip().split()]
        print(findMinSum(arr,brr,n))
    t-=1