def minFlips(S):
        # Code here
        flip=0
        for i in range(len(S)):
            if i%2==0:
                if S[i]=='0':
                    flip+=1
            if i%2!=0:
                if S[i]=='1':
                    flip+=1

        c=min(flip,(len(S)-flip))
        return c
if __name__=='__main__':
    tc=int(input())
    for _ in range(tc):
        s=input()
    print(minFlips(s))
