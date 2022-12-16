#User function Template for python3


class Solution:
    def waysToBreakNumber(self, n):
        #code here
        m=10**9+7
        return((n+1)*(n+2)//2%m)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        print(ob.waysToBreakNumber(n))
        
# } Driver Code Ends