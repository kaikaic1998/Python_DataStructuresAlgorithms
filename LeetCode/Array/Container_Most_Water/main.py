class Solution:
    def maxArea(self, height: List[int]) -> int:
        # to max area, need large length, or large numbers on both side
        # if move the pointer with larger number inwards, 
        #   won't increase area because area is limited by the smaller value
        # if move the shorter line inwards
        #   there is some changes that larger number can overcome the reduction in length

        # better: O(n) time and O(1) space complexity
        area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area
        # worst: O(n^) time and O(1) space complexity
        # area = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = max(area, min(height[i],height[j]) * (j-i))
        # return area
