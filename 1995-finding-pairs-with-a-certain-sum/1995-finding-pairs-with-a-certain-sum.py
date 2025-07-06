class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.A = Counter(nums1); self.B = Counter(nums2)
        self.num = nums2


    def add(self, index: int, val: int) -> None:
        self.B[self.num[index]] -= 1
        self.num[index] += val
        self.B[self.num[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for a in self.A:
            res += self.A[a] * self.B[tot-a]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)