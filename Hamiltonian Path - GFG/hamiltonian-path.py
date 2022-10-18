#User function Template for python3
class Solution:
    def check(self, N, M, edges): 
        #code here
        d = [[] for i in range(N+1)]
        
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
            
            
        def path(node,c,n):
            if node in v:
                return False
            if c==n:
                return True
            v.add(node)
            for cnode in d[node]:
                if path(cnode,c+1,n)==True:
                    return True
            v.remove(node)
            return False
        v =set()
        for i in range(1,N+1):
            
            if path(i,1,N)==True:
                return True
        return False
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges=[]
        e = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i],e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends