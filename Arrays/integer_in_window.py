def printFirstNegativeInteger( A, N, K):
    # code here
    i=0
    j=0
    l=[]
    ans=[]
    while(j<N):
        if(A[j]<0):
            l.append(A[j])
        if(j-i+1)<K:
            j+=1
        elif(j-i+1)==K:
            #print(l)
            if(len(l)==0):
                ans.append(0)
            else:
                #rint(ans)
                ans.append(l[0])
                #if l[0]
                if l[0]==A[i]:
                    l.remove(l[0])
            j+=1
            i+=1
    return ans
def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()