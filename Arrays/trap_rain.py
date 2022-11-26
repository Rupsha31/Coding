class Solution:
    def trappingWater(self, arr,n):
        left = 0
        right = n-1 
        l_max = 0
        r_max = 0
        result = 0
        while (left <= right):
            if r_max <= l_max:
                result += max(0, r_max-arr[right])
                r_max = max(r_max, arr[right])
                right -= 1
            else:
                result += max(0, l_max-arr[left])
                l_max = max(l_max, arr[left])
                left += 1
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()