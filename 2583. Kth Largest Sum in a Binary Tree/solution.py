# Definition for a binary tree node.
# Uncomment and use the following if needed for testing.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional['TreeNode'], k: int) -> int:
        if not root:
            return -1
        
        heap = []
        queue = deque([root])
        
        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if len(heap) < k:
                heapq.heappush(heap, level_sum)
            else:
                if level_sum > heap[0]:
                    heapq.heappushpop(heap, level_sum)
        
        return heap[0] if len(heap) == k else -1
