class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        memo = {}

        def maxSumOfNodes(index, isEven):
            if index == n:
                return 0 if isEven else float('-inf')
            if (index, isEven) in memo:
                return memo[(index, isEven)]

            noXorDone = nums[index] + maxSumOfNodes(index + 1, isEven)
            xorDone = (nums[index] ^ k) + maxSumOfNodes(index + 1, isEven ^ 1)

            memo[(index, isEven)] = max(noXorDone, xorDone)
            return memo[(index, isEven)]

        return maxSumOfNodes(0, 1)
