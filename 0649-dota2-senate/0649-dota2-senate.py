class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        res = senate
        stack = []
        
        while len(set(res)) == 2:
            res_curr =[]
            for i in res:
                if not len(stack) or stack[-1] == i:
                    stack.append(i)
                    res_curr.append(i)
                elif stack[-1] != i:
                    stack.pop()
            res = res_curr 
            
        if stack:
            return "Dire" if stack[0] == 'D' else "Radiant"
        
        return "Dire" if senate[0] == 'D' else "Radiant"
        