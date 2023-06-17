class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxArray = [0] * len(height)
        rightMaxArray = [0] * len(height)
        rainWater = 0

        leftMax = 0
        rightMax = 0

        for i, h in enumerate(height):
            leftMaxArray[i] = leftMax
            leftMax = max(leftMax, h)
            rightMaxArray[-i-1] = rightMax
            rightMax = max(rightMax, height[-i-1])

        for i, h in enumerate(height):
            waterLevel = min(leftMaxArray[i], rightMaxArray[i]) - h
            if waterLevel > 0:
                rainWater += waterLevel

        return rainWater

solution = Solution()
print('Should return 6:', solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print('Should return 9:', solution.trap([4,2,0,3,2,5]))
