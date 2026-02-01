class Solution:
    def minimumCost(self, A: List[int]) -> int:
        min_ = inf
        for i in range(1, len(A)):
            for j in range(i+1, len(A)):
                min_ = min(min_, A[i] + A[j])
        return min_+A[0]