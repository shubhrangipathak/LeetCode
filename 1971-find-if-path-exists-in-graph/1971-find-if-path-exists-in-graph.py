class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        st=[0]*n
        adj=[[]for i in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        print(adj)

        q=[source]
        st[source]=1
        while q:
            x=q.pop(0)
            l=adj[x]
            for i in l:
                if st[i]==0:
                    st[i]=1
                    q.append(i)
        
        return False if st[destination]==0 else True