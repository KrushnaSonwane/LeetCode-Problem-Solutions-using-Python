class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = -1; N = n
        while N:
            if last != N % 2:
                last = N % 2
                N //= 2
            else: return False
        return True