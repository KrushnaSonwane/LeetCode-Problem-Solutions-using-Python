class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        count = 0
        temp = ''
        l = []
        for i in range(0, len(s)):
            if count < k:
                temp += s[i]
                count += 1
            else:
                l.append(temp)
                count = 1
                temp = s[i]
        if len(temp) != 0:
            for i in range(len(temp), k):
                temp += fill
            else:
                l.append(temp)
        return l