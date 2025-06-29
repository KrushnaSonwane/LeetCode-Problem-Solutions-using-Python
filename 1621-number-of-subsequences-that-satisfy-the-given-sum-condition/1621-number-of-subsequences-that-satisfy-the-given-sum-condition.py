class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        l, r = 0, len(nums) - 1
        while r >= l:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l)
                l += 1
        return res % (10**9 + 7)