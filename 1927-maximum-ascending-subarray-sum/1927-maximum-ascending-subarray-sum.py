class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res, last, sum_ = 0, 0, 0
        for num in nums:
            if num <= last:
                sum_ = 0
            sum_ += num
            last = num
            res = max(res, sum_)
        return res