from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        queue = deque([('0000', 0)])
        visited = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            for i in range(4):
                for d in (-1, 1):
                    next_node = node[:i] + str((int(node[i]) + d) % 10) + node[i+1:]
                    if next_node not in visited and next_node not in deadends:
                        queue.append((next_node, depth + 1))
                        visited.add(next_node)
        return -1
