class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        n = len(customers)
        wait = 0 
        curr = 0 
        
        for at,t in customers:
            
            curr = max(curr, at) + t
            
            wait += (curr - at) 
        
        return wait / n