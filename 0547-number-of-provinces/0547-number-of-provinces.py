class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = 0
        res = [set() for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]==1:
                    res[i].add(j)
                    res[j].add(i)
        
        vis = [False for i in range(n)]
        for i in range(n):
            if vis[i] == True:
                continue
            
            q = []
            q.append(i)
            while(q):
                m=q.pop(-1)
                vis[m]=True
                for j in res[m]:
                    if(vis[j]!=True):
                        q.append(j)
            count += 1
        return count
       