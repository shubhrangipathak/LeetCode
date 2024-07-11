class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
    
        for char in s:
            if char == ')':
                # Collect characters until the matching '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Remove the matching '('
                if stack:
                    stack.pop()
                # Reverse the collected characters and push them back onto the stack
                stack.extend(temp)
            else:
                stack.append(char)

        # Construct the result from the stack
        return ''.join(stack)