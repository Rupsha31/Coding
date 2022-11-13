def getPairsCount(arr, n, k):
        # code here
    c=0
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==k :
                c=c+1
    return c

if __name__ == '__main__':
    tc = int(input())
    while tc >0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ans = getPairsCount(arr, n, k)
        print(ans)
        tc -=1
