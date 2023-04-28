class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        ro_to_in = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            if i + 1 < len(s) and ro_to_in[s[i]] < ro_to_in[s[i+1]]:
                num -= ro_to_in[s[i]]
            else:
                num += ro_to_in[s[i]]
        return num