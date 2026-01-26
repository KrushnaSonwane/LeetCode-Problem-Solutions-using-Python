class Solution:
    def minimumAbsDifference(self, A: List[int]) -> List[List[int]]:
        A.sort()
        min_ = inf
        for i in range(1, len(A)):
            min_ = min(min_, A[i]-A[i-1])
        res = []
        for i in range(1, len(A)):
            if A[i]-A[i-1] == min_:
                res.append([A[i-1], A[i]])
        return res