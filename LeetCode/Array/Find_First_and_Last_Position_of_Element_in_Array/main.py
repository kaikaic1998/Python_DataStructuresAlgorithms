class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(L_or_R):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    #----------------double binary search-----------------
                    #-----find left bound-----
                    if L_or_R:
                        # if left of mid is not target, then mid is the first most occurence
                        if left == mid or nums[mid - 1] != target:
                            return mid
                        # if left of mid is == target
                        else:
                            right = mid - 1
                    #-----find right bound-----
                    else:
                        # if left of mid is not target, then mid is the first most occurence
                        if right == mid or nums[mid + 1] != target:
                            return mid
                        # if left of mid is == target
                        else:
                            left = mid + 1
                    #-------------------------------------------------------
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        left_res = findBound(True) # True means finding left bound
        if (left_res == -1):
            return [-1, -1]
        right_res = findBound(False) # False means finding right bound

        return [left_res, right_res]
        
        