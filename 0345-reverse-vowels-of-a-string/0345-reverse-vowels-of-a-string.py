class Solution:
    def reverseVowels(self, s: str) -> str:
        v='aeiouAEIOU'
        l=list(s)
        i=0
        j=len(s)-1
        while(i<j):
            if l[i] in v and l[j] in v:
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
            if l[i] not in v:
                i+=1
            if l[j] not in v:
                j-=1
        return "".join(l)