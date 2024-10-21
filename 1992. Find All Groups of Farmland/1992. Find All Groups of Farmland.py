class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    r2 = i
                    while r2 + 1 < m and land[r2 + 1][j] == 1:
                        r2 += 1
                    c2 = j
                    while c2 + 1 < n and land[i][c2 + 1] == 1:
                        c2 += 1
                    for r in range(i, r2 + 1):
                        for c in range(j, c2 + 1):
                            land[r][c] = 0
                    res.append([i, j, r2, c2])
        return res
