class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            comp = target - value
            if comp in seen:
                return [i, seen[comp]]
            else:
                seen[value] = i