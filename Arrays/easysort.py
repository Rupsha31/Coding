def sort012(arr,n): 
    arr.sort()
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input(str()))
        arr=[int(x) for x in input().strip().split()]
        sort012(arr,n)
        for i in arr:
            print(i, end=' ')