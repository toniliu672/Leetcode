class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
        
        count = 0
        for i in range(n - 1):
            c = arr[i]
            for k in range(i + 1, n):
                a = prefix_xor[k] ^ prefix_xor[i]
                if a == arr[k]:
                    b = prefix_xor[k + 1] ^ prefix_xor[k]
                    if a == b:
                        count += k - i
        
        return count