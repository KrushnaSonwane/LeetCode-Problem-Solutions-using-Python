class Solution:
    def binaryGap(self, n: int) -> int:
        res, last = 0, -inf
        N = n
        while N:
            if N % 2:
                res = max(last, res)
                last = 0
            last += 1
            N //= 2
        return res