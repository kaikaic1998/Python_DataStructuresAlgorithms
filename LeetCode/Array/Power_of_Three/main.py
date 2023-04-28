class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        num = round(log(n,3))
        return  3** num == n