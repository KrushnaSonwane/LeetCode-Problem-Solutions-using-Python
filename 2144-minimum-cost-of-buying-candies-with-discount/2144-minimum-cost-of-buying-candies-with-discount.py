class Solution:
    def minimumCost(self, A: List[int]) -> int:
        res= 0; A.sort()
        i = 1
        for num in A[::-1]:
            if i % 3: res += num
            i += 1
        return res