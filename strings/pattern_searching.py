def search(text, pat):
		# code here
		if text.find(pat) >=0:
		    return 1
		else:
		    return 0
if __name__=='__main__':
    tc=int(input())
    for _ in range(tc):
        s=input()
        k=input()
    print(search(s,k))
