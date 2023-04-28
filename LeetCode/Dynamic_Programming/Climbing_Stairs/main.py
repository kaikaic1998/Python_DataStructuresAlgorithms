class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def climb(n):
            if n in cache:
                return cache[n]
            else:
                if n <= 2:
                    return n
                else:
                    cache[n] = climb(n-1) + climb(n-2)
                    return cache[n]
        return climb(n)