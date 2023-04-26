class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

        # lst = set()
        # for val in nums:
        #     if val in lst:
        #         return True
        #     lst.add(val)
        # return False