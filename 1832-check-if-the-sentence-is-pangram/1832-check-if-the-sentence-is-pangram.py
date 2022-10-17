class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d={}
        if len(sentence)<26:
            return False
        for i in sentence:
            if i not in d:
                d[i]=1 
        return len(d)==26