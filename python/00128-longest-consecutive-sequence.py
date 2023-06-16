class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsDict = set(nums)

        for num in nums:
            if num-1 not in numsDict:
                temp = 0
                while (num + temp) in numsDict:
                    temp += 1
                longest = max(longest, temp)
        return longest