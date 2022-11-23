class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        c=0
        i=0
        while i+k<=len(s):
            if int(s[i:i+k])!=0 and num%int(s[i:i+k])==0:
                c+=1
            i+=1 
        return c