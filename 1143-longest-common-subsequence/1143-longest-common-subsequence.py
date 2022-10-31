class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(s1,s2):
            m=len(s1)
            n=len(s2)
            dp=[[0 for i in range(n+1)]for j in range(m+1)]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if s1[i-1]==s2[j-1]:
                        dp[i][j]=1+dp[i-1][j-1]
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            return dp[m][n]
        return lcs(text1,text2)