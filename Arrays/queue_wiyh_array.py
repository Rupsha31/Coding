class MyQueue:
    
    #Function to push an element x in a queue.
    def __init__(self):
         self.s= []
    def push(self, x):
         
         #add code here
        self.s.append(x)
        return s
    #Function to pop an element from queue and return that element.
    def pop(self): 
         
         # add code here
        if(len(self.s) == 0):
            return -1
        else:
            m=self.s.pop(0)
            return m

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

