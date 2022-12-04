def areIsomorphic(str1,str2):
        if len(str1) != len(str2):
            return 0
        dic1 = {}
        dic2 = {}
        for i , j in zip(str1 ,str2):
            if i not in dic1 and j not in dic2:
                dic1[i] = j
                dic2[j] = i
            elif i in dic1 and j in dic2 and dic1[i] != j and dic2[j]!=i:
                
                return 0
            elif i in dic1 and j not in dic2:
                return 0
            elif i not in dic1 and j in dic2:
                return 0
        return 1
if __name__ =='__main__':
    t=int(input())
    while t > 0:
        s=input()
        p=input()
        print(areIsomorphic(s,p))
        t-=1