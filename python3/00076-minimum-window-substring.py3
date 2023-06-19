from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_count = Counter(t)
        required = len(target_count)

        left = 0
        formed = 0
        window_count = Counter()
        min_len = float('inf')
        ans = ''

        for right, char in enumerate(s):
            window_count[char] += 1

            if char in target_count and window_count[char] == target_count[char]:
                formed += 1

            while formed == required and left <= right:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left : right + 1]

                window_count[s[left]] -= 1
                if s[left] in target_count and window_count[s[left]] < target_count[s[left]]:
                    formed -= 1

                left += 1

        return ans

solution = Solution()
print('Should return "BANC":', solution.minWindow('ADOBECODEBANC','ABC'))
print('Should return "a":', solution.minWindow('a','a'))
print('Should return "":', solution.minWindow('a','aa'))