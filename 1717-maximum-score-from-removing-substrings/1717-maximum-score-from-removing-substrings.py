class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_and_count(s, sub1, sub2, points1, points2):
            stack = []
            points = 0

            for char in s:
                stack.append(char)
                if len(stack) >= 2 and stack[-2] + stack[-1] == sub1:
                    stack.pop()
                    stack.pop()
                    points += points1

            remaining_string = "".join(stack)
            stack = []

            for char in remaining_string:
                stack.append(char)
                if len(stack) >= 2 and stack[-2] + stack[-1] == sub2:
                    stack.pop()
                    stack.pop()
                    points += points2

            return points

        if x >= y:
            return remove_and_count(s, "ab", "ba", x, y)
        else:
            return remove_and_count(s, "ba", "ab", y, x)