def search (arr, n, x, k) : 
    #Complete the function
    for i in range(n):
        if arr[i] == x:
            return i
    return -1
for _ in range(0,int(input())):
    n, k = map(int , input().split())
    arr = list(map(int, input().strip().split()))
    x = int(input())
    ans = search(arr, n, x, k)
    print(ans)
