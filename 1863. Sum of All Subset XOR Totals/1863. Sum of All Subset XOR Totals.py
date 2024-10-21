class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        XOR = 0
        n = len(nums)
        for i in range(2**n):
            xor_sum = 0
            for j in range(n):
                if(i & (1<<j)):
                    xor_sum ^= nums[j]
            XOR += xor_sum
        return XOR
