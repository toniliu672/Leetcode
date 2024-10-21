class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        lower = upper = digit = 0
        replace = delete = 0
        one = two = 0

        i = 0
        while i < n:
            if password[i].islower():
                lower = 1
            elif password[i].isupper():
                upper = 1
            elif password[i].isdigit():
                digit = 1
            
            j = i
            while i < n and password[i] == password[j]:
                i += 1
            length = i - j

            if length >= 3:
                replace += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1

        missing_type = 3 - (lower + upper + digit)

        if n < 6:
            return max(missing_type, 6 - n)
        elif n > 20:
            delete = n - 20
            replace -= min(delete, one * 1) // 1
            replace -= min(max(delete - one, 0), two * 2) // 2
            replace -= max(delete - one - 2 * two, 0) // 3
            return delete + max(missing_type, replace)
        else:
            return max(missing_type, replace)
