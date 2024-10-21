class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        water = 0

        max_so_far = 0
        for i in range(n):
            left_max[i] = max_so_far
            max_so_far = max(max_so_far, height[i])


        max_so_far = 0
        for i in range(n - 1, -1, -1):
            right_max[i] = max_so_far
            max_so_far = max(max_so_far, height[i])

        for i in range(n):
            water += max(0, min(left_max[i], right_max[i]) - height[i])

        return water