class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(nums,low,high):
            while low <= high:
                
                mid = (low+high)//2 
                
                if nums[mid] == target:
                    return mid
                
                elif nums[mid] > target:
                    high = mid - 1
                    
                    
                else:
                    low = mid+1 
            return -1
                
                
        nums.sort()
        n = len(nums)
        return binary_search(nums,0,n-1)