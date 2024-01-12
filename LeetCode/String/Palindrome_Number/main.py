class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num = str(x)
        i = 0
        j = len(num) - 1
        
        while i < j:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1
        return True