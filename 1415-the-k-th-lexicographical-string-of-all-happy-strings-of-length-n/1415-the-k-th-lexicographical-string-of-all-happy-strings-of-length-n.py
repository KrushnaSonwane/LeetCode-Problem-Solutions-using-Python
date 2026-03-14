class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        arr = []
        def dfs(n, s, last):
            if n == 0: 
                arr.append(s)
                return
            for ch in 'abc':
                if last != ch:
                    dfs(n - 1, s + ch, ch)
        dfs(n, '', '')
        arr.sort()
        if len(arr) < k: return ''
        return arr[k - 1]