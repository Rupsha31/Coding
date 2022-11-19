def threeWayPartition(array, a, b):
	array.sort()
	return array
if __name__ == '__main__':
    t=int(input())
    while t > 0:
        n=int(input())
        array=list(map(int,input().strip().split()))
        a=int(input())
        b=int(input())
        ans=threeWayPartition(array, a, b)
        if len(ans) == 0:
            print(0)
        else:
            print(1)
        t-=1

