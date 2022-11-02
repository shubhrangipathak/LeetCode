class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s:
            return 0
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        n=len(s)
        x=d[letter]
        print(x)
        return int((x/n)*100)