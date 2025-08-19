class Solution:
    def zeroFilledSubarray(self, A: List[int]) -> int:
        res, count = 0, 0
        for num in A:
            count = count+1 if num == 0 else 0
            res += count
        return res