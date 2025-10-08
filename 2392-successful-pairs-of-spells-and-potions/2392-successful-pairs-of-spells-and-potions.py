class Solution:
    def successfulPairs(self, A: List[int], B: List[int], K: int) -> List[int]:
        res = []
        B.sort()
        for num in A:
            i, j = 0, len(B)-1
            mid = len(B)-1
            while j >= i:
                mid = (i+j) // 2
                if B[mid] * num < K:
                    i = mid + 1
                else:
                    j = mid - 1
            if B[mid]*num >= K:
                mid -= 1
            res.append(len(B)-mid-1)

        return res