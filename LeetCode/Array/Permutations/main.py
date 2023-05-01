class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums.copy()]

        for _ in range(len(nums)):
            pop_num = nums.pop(0)
            sub_perms = self.permute(nums)

            # add pop_num to all the list inside the list
            for add_pop in sub_perms:
                add_pop.append(pop_num)
            # concatenate new results to results
            result.extend(sub_perms)
            # add the pop_num back to nums, so can start next cycle
            nums.append(pop_num)
        
        return result
