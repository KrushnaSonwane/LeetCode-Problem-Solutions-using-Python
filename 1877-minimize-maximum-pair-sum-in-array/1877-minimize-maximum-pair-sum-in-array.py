class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res, l, r = -inf, 0, len(nums)-1
        while r > l:
            res = max(res, nums[l]+nums[r])
            l += 1; r -= 1
        return res