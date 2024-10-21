class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = 2 * (n - 1)
        time = time % cycle_length

        if time < n:
            return time + 1
        else:
            return 2 * n - time - 1
