class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #------------Sliding window: better solution O(n) time complexity------------
        result = 0
        seen = Counter()
        left = 0

        for right in range(len(s)):
            if s[right] in seen:
                # if seen, move the left pointer to next to the seen value index
                left = seen[s[right]] + 1
            # Alway updating max length between left and right pointers
            result = max(result, right - left + 1)
            # Update the seen value index to the current repeated value index
            seen[s[right]] = right

        return result

        #-------------Sliding window:  O(2n) time complexity solution---------------
        # seen = Counter()
        # left = 0
        # result = 0

        # for right in range(len(s)):
        #     right_value = s[right]
        #     seen[right_value] += 1

        #     # if more than 1 same letter
        #     while seen[right_value] > 1:
        #         left_value = s[left]
        #         seen[left_value] -= 1
        #         left += 1

        #     # record current max substring length
        #     result = max(result, right - left + 1)
        # return result