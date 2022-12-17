#User function Template for python3
import math
class Solution:    
    def maxGcd(self,N):
        #code here
        res, cnt = 1, 0
        for i in range(N, 1, -1):
            if math.gcd(i, res) == 1:
                res = res *i
                cnt += 1
            if cnt == 4:
                break
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=(int)(input())
        ob=Solution()
        print(ob.maxGcd(N))
# } Driver Code Ends