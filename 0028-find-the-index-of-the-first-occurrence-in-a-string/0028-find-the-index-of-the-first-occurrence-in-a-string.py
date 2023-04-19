class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        for i in range(n):
            if needle == haystack[i:i+len(needle)]:
                return i 
            else:
                continue
        return -1