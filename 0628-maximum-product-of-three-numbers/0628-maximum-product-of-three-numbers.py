class Solution:
    def maximumProduct(self, A: List[int]) -> int:
        A.sort()
        return max(A[0] * A[1] * A[2], A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])