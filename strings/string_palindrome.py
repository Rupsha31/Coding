def isPalindrome(S):
    str = ""
    for i in S:
        str = i + str
    if(S == str):
        return 1
    else:
        return 0

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		answer = isPalindrome(S)
		print(answer)

