class Solution:
    def twoSum(self, nums: list[int], target: int = 0) -> list[int]:
      seen = dict()
      for i, num in enumerate(nums):
         comp = target - num
         if comp in seen:
            return [i, seen[comp]]
         else:
            seen[num] = i

solution = Solution()
print('should be [0,1] or [1,0]', solution.twoSum([2,7,11,15],9))