from collections import Counter
class Solution:
    def secFrequent(self, arr, n):
        # code here
        c = Counter(arr)
        return (sorted(c, key=c.get)[-2])
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
