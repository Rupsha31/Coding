
def minJumps(arr, n):
	c=0
	i=0
	d=0
	while i < n:
	    c+=1
	    i+=arr[d]
	    d=i
	return c
	        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ans = minJumps(Arr,n)
		print(ans)
# } Driver Code Ends