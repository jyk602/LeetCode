class Solution:
    def getMoneyAmount(self, n: int) -> int:

        # Create a DP table where dp[i][j] represents the minimum cost for range [i, j]
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Iterate over lengths of ranges
        for length in range(2, n + 1):  # Length of range (2 to n)
            for start in range(1, n - length + 2):  # Start of the range
                end = start + length - 1  # End of the range
                dp[start][end] = float('inf')  # Initialize to a large number
                
                # Try every pivot in the range [start, end]
                for pivot in range(start, end + 1):
                    # Cost of choosing pivot
                    left = dp[start][pivot - 1] if pivot - 1 >= start else 0
                    right = dp[pivot + 1][end] if pivot + 1 <= end else 0
                    cost = pivot + max(left, right)  # Cost for current pivot
                    dp[start][end] = min(dp[start][end], cost)  # Take the minimum

        # The answer for the full range [1, n]
        return dp[1][n]
                
                