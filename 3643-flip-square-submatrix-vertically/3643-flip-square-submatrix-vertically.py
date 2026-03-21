class Solution:
    def reverseSubmatrix(self, A: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        l, r = x, x+k-1
        while r > l:
            for i in range(y, y+k):
                A[l][i], A[r][i] =  A[r][i], A[l][i]
            l += 1
            r -= 1
        return A