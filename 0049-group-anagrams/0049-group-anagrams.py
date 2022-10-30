class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            print("".join(sorted(i)))
            v="".join(sorted(i))
            #print(i,v,d)
            if v in d:
                d[v].append(i)
            else:
                d[v]=[i]
            
        l=[]
        print(d)
        for i in d:
            l.append(d[i])
        return l