class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        dig = "1234567890"
        for i in s:
            if i in dig:
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)
        return "".join(stack)