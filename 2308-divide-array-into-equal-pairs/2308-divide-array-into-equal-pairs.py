class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashT = {}
        for num in nums:
            if num not in hashT: hashT[num] = 1
            else: hashT[num] += 1
        for num in hashT:
            if hashT[num] % 2 == 1: return False
        return True