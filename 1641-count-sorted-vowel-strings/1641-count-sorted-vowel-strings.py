class Solution:
    def countVowelStrings(self, n: int) -> int:
        def solve(n,v):
            if n == 1:
                return v
            if v == 1:
                return 1
            return solve(n-1,v)+solve(n,v-1)
        
        return solve(n,5)