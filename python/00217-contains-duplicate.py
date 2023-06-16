class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

      numsDict = {}

      for num in nums:
        if num in numsDict:
          return True
        else:
           numsDict[num] = 1
      return False

solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))