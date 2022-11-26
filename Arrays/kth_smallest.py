def kthSmallest(arr,k):
    arr.sort()
    for i in range(k):
        if(i == k-1):
            return arr[k-1]
            i+=1
if __name__ =='__main__':
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr =[int(i) for i in input().split()]
        k=int(input())
        print(kthSmallest(arr,k))
        tc-=1
