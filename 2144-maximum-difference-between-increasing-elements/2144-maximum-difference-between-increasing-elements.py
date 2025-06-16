class Solution:
    def maximumDifference(self, A: List[int]) -> int:
        res = -1
        num = A[0]
        for i in range(1, len(A)):
            if A[i] > num:
                res = max(res, A[i]-num)
            num = min(num, A[i])
        return res