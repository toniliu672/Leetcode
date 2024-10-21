class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.max_count = 0
        def backtrack(index, used):
            if index == len(s):
                self.max_count = max(self.max_count, len(used))
                return
            for i in range(index + 1, len(s) + 1):
                substr = s[index:i]
                if substr not in used:
                    used.add(substr)
                    backtrack(i, used)
                    used.remove(substr)
        backtrack(0, set())
        return self.max_count
