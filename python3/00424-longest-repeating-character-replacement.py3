class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = dict()
        longest = 0
        l = 0

        for r in range(len(s)):
            charDict[s[r]] = charDict.get(s[r], 0) + 1
            mostFrequentChar = max(charDict, key=charDict.get)
            mostFrequentCharCount = charDict[mostFrequentChar]
            while k < r-l+1 - mostFrequentCharCount:
                charDict[s[l]] = charDict[s[l]] -1
                l += 1
            longest = max(longest, r-l+1)
        return longest

solution = Solution()
print('Should return 4:', solution.characterReplacement('ABAB', 2))
print('Should return 4:', solution.characterReplacement('AABABBA', 1))

# time complexity: O(n) / O(26*n)
# space complexity: 0(1)