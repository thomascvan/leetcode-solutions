from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      # create result dict
      result = defaultdict(list)

      # iterate over each string in the list
      for string in strs:
        # turn the string to an array that tracks each character
        word = [0] * 26
        for char in string:
          i = ord(char) - ord('a')
          word[i] += 1
        result[tuple(word)].append(string)

      # turn that dict into a tuple and try adding to result as a key
        # if it exists, append the string to the value

      # return all the values in the result
      return list(result.values())

solution = Solution()
print('Should return [["bat"],["nat","tan"],["ate","eat","tea"]]:', solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))