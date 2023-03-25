class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        i = 0
        j = n-1 

        sm = 0

        while i<j:
            sm = numbers[i] + numbers[j]

            if sm > target:
                j -= 1 
            
            elif sm < target:
                i += 1 

            else:
                return [i+1,j+1]

        
                