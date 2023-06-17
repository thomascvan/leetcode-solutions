class Solution:
    def trap(self, height: list[int]) -> int:
        leftMaxArray = [0] * len(height)
        rightMaxArray = [0] * len(height)

        leftMax = 0
        rightMax = 0

        for i in range(len(height)):
            if height[i] > leftMax:
                leftMax = height[i]

            if height[len(height)-1-i] > rightMax:
                rightMax = height[len(height)-1-i]

            leftMaxArray[i] = leftMax
            rightMaxArray[len(height)-1-i] = rightMax

        rainWater = 0
        for i in range(len(height)):
            rainWater += min(leftMaxArray[i], rightMaxArray[i]) - height[i]

        return rainWater

solution = Solution()
print('Should return 6:', solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print('Should return 9:', solution.trap([4,2,0,3,2,5]))