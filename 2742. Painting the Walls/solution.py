from typing import List

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        max_sum = n + max(t +1 for t in time) if time else n
        INF = float('inf')
        dp = [INF] * (max_sum +1)
        dp[0] = 0
        for i in range(n):
            t = time[i] +1
            c = cost[i]
            for j in range(max_sum, -1, -1):
                if j >= t and dp[j - t] + c < dp[j]:
                    dp[j] = dp[j - t] + c
        return min(dp[j] for j in range(n, max_sum +1) if dp[j] != INF)
