class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        con = 0

        for i in nums:
            if i - 1 in nums:
                continue
            else:
                n = 1
                while i + 1 in nums:
                    i += 1
                    n += 1
                con = max(con, n)

        return con
        