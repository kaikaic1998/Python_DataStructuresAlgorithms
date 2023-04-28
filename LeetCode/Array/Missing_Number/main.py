class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)

        # for val in range(len(nums)+1):
        #     if val not in nums:
        #         return val
        # return -1
        