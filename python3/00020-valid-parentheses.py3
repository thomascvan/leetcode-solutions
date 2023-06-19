class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        parensDict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in parensDict:
                if stack and stack[-1] == parensDict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


solution = Solution()
print('Should return True:', solution.isValid('()'))
print('Should return True:', solution.isValid('()[]{}'))
print('Should return False:', solution.isValid('()[](]'))
print('Should return False:', solution.isValid(']'))