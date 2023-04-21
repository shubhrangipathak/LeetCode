class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d = {"1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "0":0}
        
        int_a = 0
        int_b = 0
        
        for num in num1:
            a = d[num]
            int_a = int_a*10 + a
            
        for num in num2:
            b = d[num]
            int_b = int_b*10 + b
            
        return str(int_a*int_b)
                