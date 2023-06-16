class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # if len(s) != len(t): return False

      # count = dict()

      # for char in s:
      #     if char in count:
      #       count[char] += 1
      #     else:
      #        count[char] = 1

      # for char in t:
      #   if char in count and count[char] > 0:
      #      count[char] -= 1
      #   else:
      #      return False

      # return True
      from collections import Counter
      return Counter(s) == Counter(t)


solution = Solution()
# print(solution.isAnagram('anagram','nagaram'))
print(solution.isAnagram('ab','a'))