class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        f = 0
        arr.sort()
        d = arr[1] - arr[0]
        if len(arr) == 2:
            return True
        for i in range(2,len(arr)):
            if arr[i] - arr[i-1] != d:
                return False
        return True