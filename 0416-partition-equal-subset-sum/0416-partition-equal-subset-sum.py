class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_ = sum(nums)
        if sum_ % 2 == 1: return False
        sum_ //= 2
        dp = [False for _ in range(sum_ + 1)]
        dp[0] = True
        for i in range(1, len(nums)):
            curr = [False for _ in range(sum_ + 1)]
            curr[0] = True
            for t in range(0, sum_ + 1):
                notTake = dp[t]
                take = False
                if nums[i] <= t:
                    take = dp[t - nums[i]]
                curr[t] = take or notTake
            dp = curr
        return dp[-1]
