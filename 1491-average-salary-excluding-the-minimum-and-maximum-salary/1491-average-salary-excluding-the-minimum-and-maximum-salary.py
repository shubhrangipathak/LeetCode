class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        s=salary[1:len(salary)-1]
        return sum(s)/(len(salary)-2)