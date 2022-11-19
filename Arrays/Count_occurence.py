def countOccurence(arr,n,k):
        #Your code here
        c = int(n/k)
        dic={}
        for i in arr:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        count=0
        for key in dic:
            if dic[key] > c:
                count+=1
        return count
if __name__ == '__main__':
    t=int(input())
    while t >0:
        n=int(input())
        arr=list(map(int,input().strip().split()))
        a=int(input())
        print(countOccurence(arr,n,a))
        t-=1