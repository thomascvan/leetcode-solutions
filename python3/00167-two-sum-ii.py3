class Solution:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    l = 0
    r = len(numbers) - 1

    while numbers[l] + numbers[r] != target:
      if numbers[l] + numbers[r] > target:
        r -= 1
      else:
        l += 1
    return [l+1, r+1]

solution = Solution()
print('Should return [1,2]:', solution.twoSum([2,7,11,15], 9))
print('Should return [1,3]:', solution.twoSum([2,3,4], 6))
print('Should return [1,2]:', solution.twoSum([-1,0], -1))