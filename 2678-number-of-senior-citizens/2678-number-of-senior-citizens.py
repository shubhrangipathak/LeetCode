class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for val in details if int(val[11:13]) > 60)
        