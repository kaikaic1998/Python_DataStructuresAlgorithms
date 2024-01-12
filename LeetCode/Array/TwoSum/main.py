class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        result = []
        for i, num in enumerate(nums):
            comp = target - num
            if comp in map:
                return[map[comp], i]
            map[num] = i
        return result