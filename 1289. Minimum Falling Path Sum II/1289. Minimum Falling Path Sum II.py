class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = grid[0]
        for i in range(1, n):
            new_dp = [float('inf')] * n
            
            for j in range(n):
                min_prev = min(dp[:j] + dp[j+1:])
                new_dp[j] = grid[i][j] + min_prev
            dp = new_dp
        return min(dp)