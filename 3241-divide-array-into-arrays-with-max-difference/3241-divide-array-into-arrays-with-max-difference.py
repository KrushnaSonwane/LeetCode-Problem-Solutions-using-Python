class Solution:
    def divideArray(self, A: List[int], k: int) -> List[List[int]]:
        A.sort(); res = []
        for i in range(0, len(A), 3):
            if A[i+2] - A[i] > k: return []
            res.append([A[i], A[i+1], A[i+2]])
        return res