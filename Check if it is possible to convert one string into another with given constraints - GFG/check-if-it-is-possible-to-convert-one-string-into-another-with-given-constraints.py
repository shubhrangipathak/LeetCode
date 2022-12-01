#User function Template for python3

class Solution:
    def isItPossible(sef, S, T, M, N):
        s1 = ''
        s2 = ''
        for i in S:
            if i == 'A' or i == 'B':
                s1+=i 
        for j in T:
            if j == 'A' or j == 'B':
                s2 += j 
        if s1 == s2:
            return 1
        else:
            return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S,T=input().split()
        ob=Solution()
        print(ob.isItPossible(S,T,len(S),len(T)))
# } Driver Code Ends