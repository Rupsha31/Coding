class Solution:
    def maxSubstring(self, S):
	# code here
        if "0" not in S:
            return -1
        ans = -1
        num = 0
        for i in S:
            if i == "0":
                num += 1
            else:
                num -= 1
            ans = max(ans, num)
            if num<0:
                num = 0
        return ans
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)