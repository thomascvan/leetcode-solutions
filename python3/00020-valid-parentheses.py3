class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        parensDict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for i in range(len(s)):
            if (s[i] in parensDict and len(stack) == 0) or (s[i] in parensDict and stack[-1] != parensDict[s[i]]):
                return False
            elif s[i] in parensDict and stack[-1] == parensDict[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0

solution = Solution()
print('Should return True:', solution.isValid('()'))
print('Should return True:', solution.isValid('()[]{}'))
print('Should return False:', solution.isValid('()[](]'))
print('Should return False:', solution.isValid(']'))