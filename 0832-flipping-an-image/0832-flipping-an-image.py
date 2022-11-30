class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        s=[]
        m=len(image)
        n=len(image[0])
        for i in image:
            s.append(i[::-1])
        #print(s)
        for i in range(m):
            for j in range(n):
                if s[i][j]==0:
                    s[i][j]=1
                else:
                    s[i][j]=0

        return s
        