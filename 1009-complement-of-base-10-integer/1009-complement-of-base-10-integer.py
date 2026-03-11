class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        res = []
        while n:
            res.append(n % 2)
            n //= 2
        curr, num = 0, 0
        for val in res:
            if not val: num += pow(2, curr)
            curr += 1
        return num