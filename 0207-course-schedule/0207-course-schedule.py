class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        
        adj = [[] for i in range(numCourses)]
        
        for i,j in prerequisites:
            adj[j].append(i)
            in_degree[i] += 1
            
        queue = []
        res = []
        count = 0 
        
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            x = queue.pop(0)
            res.append(x)
            count += 1 
            lst = adj[x]
            
            for y in lst:
                in_degree[y] -= 1 
                if in_degree[y] == 0:
                    queue.append(y)
        
        
        if numCourses == count:
            return True
        
        return False

