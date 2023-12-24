class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '[', '{']
        close = [')', ']', '}']

        for bracket in s:
            if bracket in open:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != open[close.index(bracket)]:
                    return False
        return True if len(stack) == 0 else False
        