class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        count = 0
        for letter in s:
            if letter == '(':
                count += 1
            elif letter == ')':
                count -= 1
            if count >= 0:
                res += letter
            else: count = 0

        temp = ""
        for i in range(len(res)-1, -1, -1):
            if res[i] == '(' and count > 0:
                count -= 1
            else:
                temp += res[i]
        return temp[::-1]