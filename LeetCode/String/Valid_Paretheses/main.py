class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for val in s:
            if val == '(' or val == '[' or val == '{':
                lst += val
            else:
                if not lst:
                    return False
                if val == ')' and lst[-1] != '(':
                    return False
                if val == '}' and lst[-1] != '{':
                    return False
                if val == ']' and lst[-1] != '[':
                    return False
                lst.pop()
        return not lst