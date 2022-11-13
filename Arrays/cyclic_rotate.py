def rotate(arr,n):
    i=0
    j=len(arr)-1
    while i != j:
        tmp=arr[i]
        arr[i]=arr[j]
        arr[j]=tmp
        i+=1
if __name__ == '__main__':
    t=int(input())
    while t > 0:
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        rotate(arr,n)
        for i in arr:
            print(i, end=' ')
        t-=1
    