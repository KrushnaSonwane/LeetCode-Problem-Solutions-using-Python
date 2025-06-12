class Solution:
    def maxAdjacentDistance(self, A: List[int]) -> int:
        res = 0
        for i in range(1, len(A)):
            res = max(res, abs(A[i]-A[i-1]))
        return max(res, abs(A[-1]-A[0]))