class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        temp = set()
        
        for i in arr:
            if i / 2 in temp or i * 2 in temp: 
                return True
            
            temp.add(i)
            
        return False