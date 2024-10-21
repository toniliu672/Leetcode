class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                substr = []
                while stack and stack[-1] != '(':
                    substr.append(stack.pop())
                stack.pop()
                stack.extend(substr)
            else:
                stack.append(char)
        
        return ''.join(stack)
