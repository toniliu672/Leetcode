class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i, n = 0, len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                for elem, cnt in top.items():
                    stack[-1][elem] += cnt * multiplicity
            elif formula[i].isalpha():
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[i_start:i]
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                stack[-1][elem] += multiplicity
            else:
                i += 1
        
        result = ""
        for elem in sorted(stack[-1].keys()):
            result += elem
            if stack[-1][elem] > 1:
                result += str(stack[-1][elem])
        
        return result