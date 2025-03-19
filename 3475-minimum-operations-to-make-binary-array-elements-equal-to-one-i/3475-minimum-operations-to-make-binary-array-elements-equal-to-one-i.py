class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(2, len(nums)):
            if nums[i-2] == 0:
                nums[i-2] = 1
                if nums[i-1] == 0:
                    nums[i-1] = 1
                else:
                    nums[i-1] = 0
                if nums[i] == 0:
                    nums[i] = 1
                else:
                    nums[i] = 0
                res += 1
            # print(nums)
        return res if nums.count(1) == len(nums) else -1
                