def majorityElement(A, N):
        #Your code here
        if N ==1:
            return A[0]
        A.sort()
        k = 1
        for i in range(len(A) - 1):
            if A[i] == A[i+1]:
                k = k + 1
            else:
                k = 1
            if k > N/2:
                return A[i]
        return -1
if __name__ == '__main__':
    tc=int(input())
    while tc > 0:
        n=int(input())
        A=[int(j) for j in input().split()]
        print(majorityElement(A,n))
        tc-=1