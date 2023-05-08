class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        arr = [i for i in range(1,n+1)]
        
        while True:
            if time >= n:
                time -= n-1
            else:
                return arr[time]
            
            arr = arr[::-1]