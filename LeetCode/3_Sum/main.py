class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1

            if i == 0 or nums[i-1] != nums[i]:
                while left < right:
                    sum_num = nums[i] + nums[left] + nums[right]
                    if sum_num > 0:
                        right -= 1
                    elif sum_num < 0:
                        left += 1
                    else:
                        result.append([ nums[i], nums[left], nums[right] ])
                        right -= 1
                        left += 1
                        while nums[left-1] == nums[left] and left < right:
                            left += 1
        
        return result
        