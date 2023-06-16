class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t): return False
      count = dict()

      for char in s:
          if char in count:
            count[char] += 1
          else:
             count[char] = 1

      for char in t:
        if char in count and count[char] > 0:
           count[char] -= 1
        else:
           return False
      return True

      # Solution that uses collections.Counter
      '''
      from collections import Counter
      return Counter(s) == Counter(t)
      '''


solution = Solution()
print('should be True:', solution.isAnagram('anagram','nagaram'))
print('should be False:', solution.isAnagram('ab','a'))