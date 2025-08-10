class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = Counter(str(n))
        
        for i in range(30):
            powerOfTwo = str(1 << i)
            if digits == Counter(powerOfTwo):
                return True
        return False