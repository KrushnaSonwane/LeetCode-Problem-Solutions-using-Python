class Solution:
    def hasSameDigits(self, s: str) -> bool:
        A = [int(ch) for ch in s]
        while len(A) > 2:
            B = []
            for i in range(len(A)-1):
                B.append((A[i]+A[i+1]) % 10)
            A = B
        return A[0] == A[1]