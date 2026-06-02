class Solution:
    def isValid(self, s: str) -> bool:
        brackets={'}':'{',']':'[',')':'('}
        stack=[]
        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            elif not stack or stack.pop()!=brackets[bracket]:
                    return False
        return not stack

        