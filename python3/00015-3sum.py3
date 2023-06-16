class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
      result = []
      nums.sort()

      for a in range(len(nums) - 2):
        if a > 0 and nums[a] == nums[a - 1]:
            continue
        l = a + 1
        r = len(nums) - 1
        first = nums[a]

        while l < r:
          total = first + nums[l] + nums[r]
          if total == 0:
            result.append([first, nums[l], nums[r]])
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            l += 1
            r -= 1
          elif total > 0:
            r -= 1
          else:
            l += 1
      return result


solution = Solution()
print('Should return [[-1,-1,2],[-1,0,1]]:', solution.threeSum([-1, 0, 1, 2, -1, -4]))
print('Should return []:', solution.threeSum([0, 1, 1]))
print('Should return [[0,0,0]]:', solution.threeSum([0, 0, 0]))

solution = Solution()
print('Should return [[-1,-1,2],[-1,0,1]]:', solution.threeSum([-1,0,1,2,-1,-4]))
print('Should return []:', solution.threeSum([0,1,1]))
print('Should return [[0,0,0]]:', solution.threeSum([0,0,0]))