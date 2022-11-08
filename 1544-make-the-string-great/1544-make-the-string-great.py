class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack and stack[-1]!=i and (stack[-1]==i.lower() or stack[-1]==i.upper()):
                stack.pop()
            else:
                stack.append(i)
            print(stack)
        return "".join(stack)