class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        dic = Counter(nums1)
        result = []
        for val in nums2:
            if dic[val] > 0:
                dic[val] -= 1
                result.append(val)
        return result