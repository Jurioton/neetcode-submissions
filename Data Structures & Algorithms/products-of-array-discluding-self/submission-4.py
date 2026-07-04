class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right=[0]*len(nums)
        left=[0]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                left[i] = 1
                continue
            left[i] = nums[i-1] * left[i-1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right[i] = 1
                continue
            right[i] = nums[i + 1] * right[i + 1]
        return [x * y for x, y in zip(left, right)]