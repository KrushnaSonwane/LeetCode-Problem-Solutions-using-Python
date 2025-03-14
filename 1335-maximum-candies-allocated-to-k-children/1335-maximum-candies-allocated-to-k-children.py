class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        if sum(candies) < k: return 0
        low, high = 1, sum(candies)
        ans = low
        
        def isValid(mid):
            curr = 0
            for candy in candies:
                if candy < mid: continue
                else: curr += candy // mid
            return curr

        while high >= low:
            mid = (high + low) // 2
            curr = isValid(mid)
            if curr >= k:
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1
        return ans