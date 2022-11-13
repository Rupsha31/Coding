def push(l,n,k):
    if(len(l)>n):
        print("stack overflow")
        exit(0)
    else:
        l.append(k)
def pop(l):
    if(len(l)== 0):
        print("stack underflow")
        exit(0)
    else:
        print(l.pop(0))

if __name__== '__main__':
    l=[]
    n=int(input()) #max size of stack
    j=int(input())  #actual size of stack
    for i in range(j):
        k=int(input())
        push(l,n,k)
    m=int(input()) #number of elements to pop
    for i in range (m):
        pop(l)