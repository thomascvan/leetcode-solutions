class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
      # 1  2  3  4
      # 1  2  6  24
      # 24 24 12 4

      prefix = 1
      postfix = 1

      res = [1] * (len(nums))

      for i in range(len(nums)):
          res[i] = prefix
          prefix *= nums[i]

      for i in range(len(nums) -1, -1, -1):
          res[i] *= postfix
          postfix *= nums[i]

      return res

solution = Solution()

print('Should return [24,12,8,6]:', solution.productExceptSelf([1,2,3,4]))