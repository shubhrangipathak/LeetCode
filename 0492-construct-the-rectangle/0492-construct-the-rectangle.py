class Solution:
    def constructRectangle(self, area: int) -> List[int]:
#         w=int(math.sqrt(area))
#         while(area%w!=0):
#             w-=1
#         return [area//w,w]
        l=w=int(sqrt(area))
        while(w>0):
            ans=l*w
            if ans==area:
                return [l,w]
            elif ans>area:
                w-=1
            else:
                l+=1
    