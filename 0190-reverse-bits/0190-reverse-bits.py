class Solution:
    def reverseBits(self, n: int) -> int:
        A = [0 for i in range(32)]; num = n
        i, res = 0, 0
        while num:
            A[i] = num%2
            num //= 2
            i += 1
        for i, num in enumerate(A[::-1]):
            res += (2 ** i) * num
        return res