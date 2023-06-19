class Solution:
    def check_keys_occurrence_in_string(self, obj, string):
        for key, count in obj.items():
            if string.count(key) != count:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        charDict = {}
        length = len(s1)
        for char in s1:
            charDict[char] = charDict.get(char, 0) + 1
        for l in range(len(s2) - length + 1):
            if self.check_keys_occurrence_in_string(charDict, s2[l:l+length]):
                return True
        return False

solution = Solution()
print('Should return True:',solution.checkInclusion('ab','eidbaooo'))
print('Should return False:',solution.checkInclusion('ab','eidboaoo'))