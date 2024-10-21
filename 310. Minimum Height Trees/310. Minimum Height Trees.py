class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        leaves = [i for i in range(n) if degree[i] == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                for nei in graph[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        new_leaves.append(nei)
            leaves = new_leaves
        return leaves