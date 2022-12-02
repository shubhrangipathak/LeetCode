class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return 0
        d1={}
        d2={}
        l1=[]
        l2=[]
        for i in word1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for j in word2:
            if j not in d1:
                return False
            if j in d2:
                d2[j]+=1 
            else:
                d2[j]=1
        
        for i,j in zip(d1,d2):
            l1.append(d1[i])
            l2.append(d2[j])
        l1.sort()
        l2.sort()
        return l1==l2
        
    