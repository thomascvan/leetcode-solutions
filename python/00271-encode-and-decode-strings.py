class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strings):
      # write your code here
      result = ''
      for string in strings:
          result += f'{len(string)}:{string}'
      return result
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, string):
      # write your code here
      result, i = [], 0

      while i < len(string):
        j = i
        while string[j] != ':':
          j += 1
        length = int(string[i:j])
        result.append(string[j+1: j+1+length])
        i = j+1+length
      return result



solution = Solution()
strings = ["lint", "code", "love", "you"]
string = solution.encode(strings)

print(strings == solution.decode(string))