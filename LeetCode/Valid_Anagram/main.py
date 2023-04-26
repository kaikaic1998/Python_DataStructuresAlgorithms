from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # ss = sorted(s)
        # tt = sorted(t)
        # return ss == tt