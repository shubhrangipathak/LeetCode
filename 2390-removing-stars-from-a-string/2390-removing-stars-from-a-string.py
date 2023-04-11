class Solution:
    def removeStars(self, s: str) -> str:
        if len(s)<=1:
            if len(s) and s[0]!='*':
                return s[0]
            else:
                return ""
                
        stack = []
        for i in s:
            if i!='*':
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)
        