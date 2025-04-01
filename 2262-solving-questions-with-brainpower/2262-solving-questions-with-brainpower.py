class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            if n > questions[i][1] + i + 1:
                dp[i] = max(questions[i][0] + dp[questions[i][1] + i + 1], dp[i + 1])
            else:
                dp[i] = max(questions[i][0], dp[i + 1])
        return dp[0]