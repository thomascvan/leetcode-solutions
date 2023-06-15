class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsDict = {}

        for num in nums:
            numsDict[num] = 1
        for num in nums:
            if num-1 not in numsDict:
                temp = 0
                val = num
                while val in numsDict:
                    temp += 1
                    val += 1
                if temp > longest:
                    longest = temp
        return longest