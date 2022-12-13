#User function Template for python3
class Solution:

    def findRange(self,arr, size):
        # code here
        l = 0
        count = 0
        res = (0, 0, 0)
        for r in range(n):
            count += 1 if arr[r] == '0' else -1
            while count < 0:
                count -= 1 if arr[l] == '0' else -1
                l += 1
            res = max(res, (count, -(l+1), -(r+1)))
        
        return [-1] if res[0] == 0 else  [-res[1] , -res[2]]


#{ 
 # Driver Code Starts
if __name__ == '__main__': 


	tc=int(input())
	while tc > 0:
	    n=int(input())
	    s=input()
	    ob = Solution()
	    ans = ob.findRange(s, n)
	    if len(ans)==1:
	        print(ans[0])
	    else:
	        print(str(ans[0])+" "+str(ans[1]))
	    tc=tc-1
# } Driver Code Ends