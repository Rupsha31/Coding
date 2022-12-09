def ispar(x):
    # code here
    if len(x)==1:
        return False
    st=[]
    for ch in x:
        if ch=='(' or ch=='{' or ch=='[':
            st.append(ch)
        elif ch==')' and len(st)>0 and st[-1]=='(':
            st.pop()
        elif ch=='}' and len(st)>0 and  st[-1]=='{':
            st.pop()
        elif ch==']' and len(st)>0 and st[-1]=='[':
            st.pop()
        else:
            return False
    return len(st)==0
if __name__=='__main__':
    tc=int(input())
    while tc>0:
        s=input()
        if ispar(s):
            print('balanced')
        else:
            print('not balanced')
        tc-=1
