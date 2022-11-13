def maximize(arr,n):
    arr.sort()
    s=0
    for i in range(n):
        s=s+(i*arr[i])
    return s % 1000000007
if __name__== '__main__':
    t= int(input())
    while t != 0:
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        print(maximize(arr,n))
