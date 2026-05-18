class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hashT = {}
        for i, num in enumerate(arr):
            if num not in hashT:
                hashT[num] = [i]
            else:
                hashT[num].append(i)
        visit = set()
        visit.add(0)
        n = len(arr)
        queue = [0]
        res = 0
        while queue:
            for _ in range(len(queue)):
                index = queue.pop(0)
                if index - 1 >= 0 and arr[index - 1] in hashT:
                    queue.append(index - 1)
                if index + 1 == n: return res
                if index + 1 < n and arr[index + 1] in hashT:
                    queue.append(index + 1)
                if arr[index] in hashT:
                    for i in hashT[arr[index]]:
                        if i != index: queue.append(i)
                    del hashT[arr[index]]
            res += 1
        return res