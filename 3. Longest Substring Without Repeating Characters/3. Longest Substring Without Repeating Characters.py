class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        start = 0

        for end, ch in enumerate(s):
            if ch in char_map and char_map[ch] >= start:
                start = char_map[ch] + 1
            char_map[ch] = end
            max_length = max(max_length, end - start + 1)

        return max_length
