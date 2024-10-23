# Definition for a binary tree node.
# Uncomment and use the following if needed for testing.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        if not root:
            return None
        
        queue = deque([(root, None)])  # Each element is a tuple (node, parent)
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            parent_map = defaultdict(int)
            total_sum = 0
            
            # Collect all nodes and their parents at the current level
            for _ in range(level_size):
                node, parent = queue.popleft()
                level_nodes.append((node, parent))
                total_sum += node.val
                if parent:
                    parent_map[parent] += node.val
                else:
                    parent_map[parent] += node.val  # For root, parent is None
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            
            # Replace each node's value with the sum of cousins
            for node, parent in level_nodes:
                if parent is None:
                    # Root node has no cousins
                    node.val = 0
                else:
                    node.val = total_sum - parent_map[parent]
        
        return root
