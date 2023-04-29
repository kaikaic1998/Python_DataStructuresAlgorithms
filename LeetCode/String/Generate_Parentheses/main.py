class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        # More concise solution: pass string + "(" or ")" when recursive call
        def make_par(left, right, strs):
            if left == right == n:
                result.append(strs)
                return
            if left < n:
                make_par(left+1, right, strs + '(')
            if right < left:
                make_par(left, right+1, strs + ')')

        # Solution: use list to store current parenthesis, pop added after done
        # par = []
        # def make_par (left, right, strs):
        #     par.append(strs)
        #     if left == right == n:
        #         result.append(''.join(par))
        #         return
        #     if left < n:
        #         make_par(left+1, right, '(')
        #         par.pop()
        #     if right < left:
        #         make_par(left, right+1, ')')
        #         par.pop()
            
        make_par(0, 0, '')
        return result