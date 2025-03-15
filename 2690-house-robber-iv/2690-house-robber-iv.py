class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def checkValid(currMoney):
            lastIndex, count = -2, 0
            for i, money in enumerate(nums):
                if currMoney >= money and i - 1 != lastIndex:
                    count += 1
                    lastIndex = i
            return count >= k
        l, r = 1, max(nums)
        while r > l:
            mid = (r + l) // 2
            if checkValid(mid):
                r = mid
            else:
                l = mid + 1
        return l