class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        neg = []
        pos = []
        neg_sum = 0
        pos_sum = 0
        res = 0
        k = 1
        
        for i in satisfaction:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        
        for i in neg:
            neg_sum += (abs(i))
        pos_sum = sum(pos)
        
        neg.sort(reverse=True)
        pos.sort()
        
        while neg_sum > pos_sum:
            val = neg.pop()
            neg_sum -= abs(val) 
            
            if neg_sum < pos_sum:
                break
        
        neg[:] = neg[::-1]
        l = neg + pos
        
        for i in l:
            res += (i * k)
            k += 1
        
        return res


