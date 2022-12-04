def removeDuplicates(str):
	str1=""
	for i in range(len(str)):
	    if str[i] not in str1:
	        str1=str1+str[i]
	return str1
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ans = removeDuplicates(str)
        print(ans)
        tc -= 1

