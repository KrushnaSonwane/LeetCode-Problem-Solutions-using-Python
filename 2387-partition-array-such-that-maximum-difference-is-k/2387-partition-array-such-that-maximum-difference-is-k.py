class Solution:
    def partitionArray(self, A: List[int], k: int) -> int:
        A.sort()
        res, last = 1, A[0]
        for num in A:
            if num - last > k: 
                res, last = res + 1, num
        return res