class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i, h_val in enumerate(haystack):
            if h_val == needle[0]:
                sub = haystack[i:i+len(needle)]
                if sub == needle:
                    return i
        return -1