def minimumNumberOfSwaps(S):
        # code here 
        c=0
        open=0
        for i in S:
            if i == '[':
                open+=1
            else:
                open-=1
                if open < 0:
                    c=c-open
        return c
if __name__=='__main__':
    tc=int(input())
    while tc>0:
        s=input()
        print(minimumNumberOfSwaps(s))
        tc-=1