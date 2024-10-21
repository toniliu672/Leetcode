class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_positions = collections.defaultdict(list)
        for i, char in enumerate(ring):
            char_positions[char].append(i)

        n, m = len(ring), len(key)
        dp = [[float('inf')] * n for _ in range(m)]

        for start in char_positions[key[0]]:
            dp[0][start] = min(start, n - start) + 1

        for i in range(1, m):
            for start in char_positions[key[i]]:
                for prev_start in char_positions[key[i - 1]]:
                    steps = min(abs(start - prev_start), n - abs(start - prev_start))
                    dp[i][start] = min(dp[i][start], dp[i - 1][prev_start] + steps + 1)

        return min(dp[m - 1])