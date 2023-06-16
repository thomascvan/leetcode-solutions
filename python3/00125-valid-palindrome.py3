class Solution:
  def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    l = 0
    r = len(s)-1

    while (l < r):
      while (l < r and not self.isAlphaNum(s[l])):
        l += 1
      while (l < r and not self.isAlphaNum(s[r])):
        r -= 1
      if s[l] == s[r]:
        l += 1
        r -= 1
      else:
        return False
    return True

  def isAlphaNum(self, c):
    return (ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9'))

solution = Solution()
print('Should return True:', solution.isPalindrome("A man, a plan, a canal: Panama"))