class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)  
        total = 0
        for i in range(k):
            curr = happiness[i] - (i)  
            total += max(curr, 0)  
        return total