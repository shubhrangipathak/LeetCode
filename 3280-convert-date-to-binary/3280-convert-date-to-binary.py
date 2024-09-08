class Solution:
    def convertDateToBinary(self, date: str) -> str:
    
        st = date.split('-')
        res = []

        for char in st:
            b = bin(int(char))
            res.append(b[2:])
        
        return '-'.join(res)