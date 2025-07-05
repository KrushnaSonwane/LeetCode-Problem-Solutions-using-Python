class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hashT = collections.Counter(arr)
        res = -1
        for num in hashT:
            if num == hashT[num]:
                res = max(res, num)
        return res