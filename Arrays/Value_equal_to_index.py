def valuequal(A,n):
    l=[]
    for i in range(n):
        if i+1 == A[i]:
            l.append(i+1)
    return l
if __name__=='__main__':
    t=int(input())
    while t > 0:
        n=int(input())
        A=list(map(int,input().strip().split()))
        ans=valuequal(A,n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x,end=" ")
            print()
        t-=1