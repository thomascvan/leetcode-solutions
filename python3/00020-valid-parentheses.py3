class Solution:
    def isValid(self, s: str) -> bool:
        return

solution = Solution()
print('Should return True:', solution.isValid('()'))
print('Should return True:', solution.isValid('()[]{}'))
print('Should return False:', solution.isValid('()[](]'))
print('Should return False:', solution.isValid(']'))