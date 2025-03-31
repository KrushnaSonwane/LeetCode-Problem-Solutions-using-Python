class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        hashT = {}
        count = 0
        for ch in s:
            if ch not in hashT:
                hashT[ch] = 1
            else:
                hashT[ch] += 1
        ans = []
        arr = set()
        currLen = 0
        for ch in s:
            if ch not in arr:
                arr.add(ch)
                count += 1
            hashT[ch] -= 1
            currLen += 1
            if hashT[ch] == 0:
                count -= 1
            if count == 0:
                ans.append(currLen)
                currLen = 0
        return ans