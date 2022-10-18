class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # temp=[]
        # ps=[0]*len(nums)
        # ps[0]=nums[0]
        # for i in range(1,len(nums)):
        #     ps[i]=ps[i-1]+nums[i]
        # print(ps)
        # for i in range(len(nums)):
        #     if nums[i]==1:
        #         temp.append(i)
        # print(temp)
        # for i in range(1,len(temp)):
        #     temp[i]+=temp[i-1]
        # print(temp)
        # l=0
        # r=l+k
        ###########################################33
        pos=[]
        for i in range(len(nums)):
            if nums[i]==1:
                pos.append(i)
        print(pos)
        psm=[0]*len(pos)
        for i in range(len(pos)):
            if i==0:
                psm[i]=pos[i]+0
            else:
                psm[i]=pos[i]+psm[i-1]
        print(psm)
        l=0
        r=k-1
        tot_mov=0
        ans=float("inf")
        while r<len(pos):
            if k%2!=0:
                m=l+(k//2)
                rsum=psm[r]-psm[m]
                if m==0:
                    l1=0
                else:
                    l1=psm[m-1]
                if l==0:
                    l2=0
                else:
                    l2=psm[l-1]
                lsum=l1-l2
                #lsum=(m==0?0:psm[m-1])-(l==0?0:psm[l-1])
                tot_mov=rsum-lsum
                rad=m-l
                saves=(rad*(rad+1))
                print(tot_mov-saves)
                ans=min(ans,tot_mov-saves)
                print(ans)
            elif k%2==0:
                m=(l+(k//2)-1)
                rsum=psm[r]-psm[m]
                if m==0:
                    l1=0
                else:
                    l1=psm[m-1]
                if l==0:
                    l2=0
                else:
                    l2=psm[l-1]
                lsum=l1-l2
                #lsum=(m==0?0:psm[m-1])-(l==0?0:psm[l-1])
                tot_mov=rsum-lsum-pos[m]
                rad=m-l
                saves=(rad*(rad+1))+(rad+1)
                print(tot_mov-saves)
                ans=min(ans,tot_mov-saves)
                print(ans)
            l+=1 
            r+=1
        return ans
            
        