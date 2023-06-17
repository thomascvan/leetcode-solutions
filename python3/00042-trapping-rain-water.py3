class Solution:
    def trap(self, height: list[int]) -> int:
        leftMaxArray = [0] * len(height)
        rightMaxArray = [0] * len(height)

        leftMax = 0
        rightMax = 0

        for i, h in enumerate(height):
            if h > leftMax:
                leftMax = h
            leftMaxArray[i] = leftMax

        for i, h in reversed(list(enumerate(height))):
            if h > rightMax:
                rightMax = h
            rightMaxArray[i] = rightMax

        rainWater = 0
        for i, h in enumerate(height):
            rainWater += min(leftMaxArray[i], rightMaxArray[i]) - h

        return rainWater


solution = Solution()
print('Should return 6:', solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print('Should return 9:', solution.trap([4,2,0,3,2,5]))
