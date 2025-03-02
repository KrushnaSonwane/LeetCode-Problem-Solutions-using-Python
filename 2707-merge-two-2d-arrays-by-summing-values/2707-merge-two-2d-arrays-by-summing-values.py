class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        arr = set()
        hashT = {}
        for id, val in nums1:
            hashT[id] = val
            arr.add(id)
        for id, val in nums2:
            if id in hashT:
                hashT[id] += val
            else:
                hashT[id] = val
                arr.add(id)
        res = []
        for id in sorted(arr):
            res.append([id, hashT[id]])
        return res