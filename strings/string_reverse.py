def reverse(S):
    str=""
    for i  in S:
        str=i+str
    return str
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
