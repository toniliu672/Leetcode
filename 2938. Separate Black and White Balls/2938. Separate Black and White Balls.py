class Solution:
    def minimumSteps(self, s: str) -> int:
        count_ones = 0
        total_swaps = 0
        for char in s:
            if char == '1':
                count_ones += 1
            elif char == '0':
                total_swaps += count_ones
        return total_swaps
