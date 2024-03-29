class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        a=len(s)
        
        dp=[[0 for i in range(a+1)] for j in range(a+1)]
        
        for i in range(1,a+1):
            for j in range(1,a+1):
                
                if s[i-1]==s[a-j]:
                    dp[i][j]=1+dp[i-1][j-1]
                    
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])  
                    
        return dp[-1][-1]