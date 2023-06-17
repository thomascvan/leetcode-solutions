class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

solution = Solution()
print('Should return 3:', solution.lengthOfLongestSubstring('abcabcbb'))
print('Should return 1:', solution.lengthOfLongestSubstring('bbbbb'))
print('Should return 3:', solution.lengthOfLongestSubstring('pwwkew'))