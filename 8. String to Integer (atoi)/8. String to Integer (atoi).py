class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i == len(s):
            return 0
        
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        result *= sign
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        
        return result