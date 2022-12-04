class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        comp1 = min(arr)
        comp2 = max(arr)
        #max sort according lexiographic value or order
        #lexiographic order accounts number oif unique character in string and if we use key=len then it returns length wise max value
        lcp = ""
        for i in range(len(comp1)):
            if comp1[i] != comp2[i]:
                break
            lcp += comp1[i]
        if lcp == "":
            return -1
        return lcp

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends