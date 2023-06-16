from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        countMap = Counter(nums)
        countList = [[] for _ in range(len(nums)+1)]
        result = []
        for key in countMap:
            countList[countMap[key]].append(key)

        for i in range(len(countList)-1,0,-1):
            for num in countList[i]:
                if len(result) < k:
                    result.append(num)
                else: break
        return result

solution = Solution()
print('Should return [1,2]:', solution.topKFrequent([1,1,1,2,2,3],2))
print('Should return [1]:', solution.topKFrequent([1],1))