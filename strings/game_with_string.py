def minValue(s, k):
        # code here
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
        value = list(dic.values())
        for i in range(k):
            val = value.index(max(value))
            value[val] = value[val]-1
        return sum([i*i for i in value])
if __name__=='__main__':
    tc=int(input())
    for _ in range(tc):
        s=input()
        k=int(input())
    print(minValue(s,k))

