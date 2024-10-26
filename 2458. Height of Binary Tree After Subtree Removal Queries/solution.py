# Definition for a binary tree node.
# Uncomment and use the following if needed for testing.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeQueries(self, root: Optional['TreeNode'], queries: List[int]) -> List[int]:
        depth = {}
        height = {}
        nodes = {}

        def dfs(node, d):
            if not node:
                return -1
            depth[node.val] = d
            nodes[node.val] = node
            left_height = dfs(node.left, d + 1)
            right_height = dfs(node.right, d + 1)
            h = max(left_height, right_height) + 1
            height[node.val] = h
            return h

        dfs(root, 0)

        from collections import defaultdict

        depth_to_heights = defaultdict(list)

        for node_val, d in depth.items():
            h = height[node_val]
            depth_to_heights[d].append((h, node_val))

        max_total_height = max(depth.values())

        for d in depth_to_heights:
            depth_to_heights[d].sort(reverse=True)

        res = []
        for q in queries:
            q_depth = depth[q]
            heights_nodes = depth_to_heights[q_depth]
            if heights_nodes[0][1] != q:
                new_height = max_total_height
            else:
                if len(heights_nodes) > 1:
                    second_height = heights_nodes[1][0]
                    new_height = second_height + q_depth
                else:
                    new_height = q_depth - 1
            res.append(new_height)
        return res
