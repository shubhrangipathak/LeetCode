class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = min(strs, key = len)
        
        for i in strs:
            for j in range(len(s)):
                if i[j] != s[j]:
                    s = i[:j]
                    break 
                
            s = min(i , s)
            
            if s == "":
                return ""
        
        return s
     
        
                    
                        