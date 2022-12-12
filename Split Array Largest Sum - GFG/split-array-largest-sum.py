#User function Template for python3

class Solution:
    def splitArray(self, arr, N, k):
        start, end = 0,0
        for i in arr:
            start = max(start, i)
            end += i
        while start < end:
            mid = start + (end - start) // 2
            
            pieces = 1
            sm = 0
            
            for ele in arr:
                if sm+ele > mid:
                    sm = ele
                    pieces += 1
                else:
                    sm += ele
            
            if pieces > k:
                start = mid + 1
            else:
                end = mid
        
        return end
       
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends