class Solution:
    def isZeroArray(self, A: List[int], Q: List[List[int]]) -> bool:
        B = [0 for _ in A]
        for l, r in Q:
            B[l] -= 1
            if r + 1< len(A):
                B[r+1] += 1
        sum_ = 0
        for i in range(len(B)):
            B[i] += sum_
            sum_ = B[i]
        for i, val in enumerate(B):
            if A[i] + val > 0: return False
        return True