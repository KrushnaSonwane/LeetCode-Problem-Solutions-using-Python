class Solution:
    def minRemoval(self, A: List[int], k: int) -> int:
        A.sort()
        res = inf
        for i in range(len(A)-1, -1, -1):
            l, r = 0, i
            key = -1
            while r >= l:
                mid = (r + l) // 2
                if A[mid] * k >= A[i]:
                    res = min(res, mid + (len(A) - (i + 1)))
                    r = mid - 1
                else:
                    l = mid + 1
        return res
