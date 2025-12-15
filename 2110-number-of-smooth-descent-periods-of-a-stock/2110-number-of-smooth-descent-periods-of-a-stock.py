class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [1 for _ in prices]
        for i, price in enumerate(prices):
            if i > 0:
                if price + 1 == prices[i - 1]: dp[i] += dp[i - 1]
        return sum(dp)