def removeDuplicates(str):
	# code here
	str1=""
	for i in range(len(str)):
	    if str[i] not in str1:
	        str1=str1+str[i]
	return str1
if __name__ == '__main__':
    t=int(input())
    while t > 0:
        str=input()
        print(removeDuplicates(str))
    t-=1
