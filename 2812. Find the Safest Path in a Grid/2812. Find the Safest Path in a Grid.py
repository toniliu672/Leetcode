class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    dist[i][j] = 0

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

        l, r = 0, min(dist[0][0], dist[n-1][n-1])
        while l < r:
            mid = (l + r + 1) // 2
            if self.bfs(grid, dist, mid):
                l = mid
            else:
                r = mid - 1

        return l

    def bfs(self, grid, dist, mid):
        n = len(grid)
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        visited = [[0] * n for _ in range(n)]
        queue = deque([(0, 0)])

        while queue:
            x, y = queue.popleft()
            if x == n - 1 and y == n - 1:
                return True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and dist[nx][ny] >= mid:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

        return False
