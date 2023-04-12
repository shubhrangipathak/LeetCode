class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        path = path.split('/')
        
        for i in path:
            
            if i == "..":
                if len(stack) != 0:
                    stack.pop()
            
            elif i == "." or i == "":
                continue
                
            else:
                stack.append(i)

                    
        return '/'+'/'.join(stack)