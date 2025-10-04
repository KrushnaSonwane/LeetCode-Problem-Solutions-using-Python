class Solution:
    def maxArea(self, A: List[int]) -> int:
        l, r = 0, len(A)-1
        res = 0
        while r > l:
            res = max(res, min(A[l], A[r]) * (r - l))
            if A[l] > A[r]:
                r -= 1
            else:
                l += 1
        return res
