class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        phone = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []

        def backtrack(combo, next_digit):
            if not next_digit:
                result.append(combo)
                return

            for letter in phone[next_digit[0]]:
                backtrack(combo + letter, next_digit[1:])
        
        backtrack('', digits)

        return result
