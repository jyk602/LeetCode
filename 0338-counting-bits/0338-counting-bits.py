class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n +1)
        ans = [0]
        offset = 1 
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i 
            dp[i] = 1 + dp[i - offset] 
            
        return dp
    
        
            
#         0 - 0000 : 0  -> dp[0] = 0
#         1 - 0001 : 1  -> dp[1] = 1 + dp[1 - 1] = 1
#         2 - 0010 : 1  -> dp[2] = 1 + dp[2 - 2] = 1
#         3 - 0011 : 2  -> dp[3] = 1 + dp[3 - 2] = 2
#         4 - 0100 : 1  -> dp[4] = 1 + dp[4 - 4] = 1
#         5 - 0101 : 2  -> dp[5] = 1 + dp[5 - 4] = 2
#         6 - 0110 : 2  -> dp[6] = 1 + dp[6 - 4] = 2
#         7 - 0111 : 3  -> dp[7] = 1 + dp[7 - 4] = 3
#         8 - 1000 : 1  -> dp[8] = 1 + dp[8 - 8] = 1
   
        