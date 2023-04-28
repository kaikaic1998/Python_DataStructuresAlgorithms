class Solution:
    def majorityElement(self, nums: List[int]) -> int:
# curr will store the current majority element
# count will store the count of the majority
        curr_max = nums[0]
        count = 1
        for i in range (1, len(nums)):
            if nums[i] == curr_max:
 # if i is equal to current majority, they're in same team, hence added, 
 # else one current majority and i both will be dead
                count += 1
            else:
                count -= 1
            # if count is 0 means King is de-throwned
            if not count:
                if i + 1 < len(nums):
                    # the next element is the new King
                    curr_max = nums[i+1]
# starting it with 0 because we can't increment the i of the for loop, the count will be 1 in next iteration, and again the battle continues after next iteration
                count = 0
        return curr_max

        # O(n) space and time complexity
        # major = len(nums) // 2
        # dic = defaultdict(int)
        # for val in nums:
        #     dic[val] += 1
        #     if dic[val] > major:
        #         return val
        # return -1