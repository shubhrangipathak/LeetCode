class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        pt1 = ord(coordinate1[0])
        num1 = int(coordinate1[1])
        
        pt2 = ord(coordinate2[0])
        num2 = int(coordinate2[1])
        
        a = (pt1 + num1) % 2 
        b = (pt2 + num2) % 2 
        
        return a == b