class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s):
            return len(s) == len(set(s))
        
        def backtrack(index, current):
            if not is_unique(current):
                return 0
            
            max_length = len(current)
            
            for i in range(index, len(arr)):
                max_length = max(max_length, backtrack(i + 1, current + arr[i]))
            
            return max_length
        
        return backtrack(0, "")