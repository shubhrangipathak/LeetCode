#User function Template for python3

from typing import List
import collections
class Solution:
    def minimumCost(self, flights: List[List[int]], n : int, k : int) -> int:
        # code here
        adj = collections.defaultdict(list)
        for u,v,w in flights:
            adj[u].append((v,w))
        dist = [-1 for _ in range(n+1)]
        q = collections.deque()
        dist[k] = 0
        q.append((k,dist[k]))
        ans = -1
        while q:
            curr = q.popleft()
            node = curr[0]
            cost = curr[1]
            
            for neighbour in adj[node]:
                new_node = neighbour[0]
                new_cost = neighbour[1]
                if dist[new_node] == -1:
                    dist[new_node] = cost + new_cost
                    q.append((new_node,dist[new_node]))
                elif dist[new_node] > cost+new_cost:
                    dist[new_node] = cost + new_cost
                    q.append((new_node,dist[new_node]))
                    
       #step-4
        for d in range(1, len(dist)):
            if dist[d] != -1:
                ans = max(ans, dist[d])
            else:
                return -1
        return ans
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        k = int(input())
        m = int(input())
        flights = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            flights.append([u, v, wt])
        obj = Solution()
        ans = obj.minimumCost(flights, n, k)
        print(ans)
            

# } Driver Code Ends