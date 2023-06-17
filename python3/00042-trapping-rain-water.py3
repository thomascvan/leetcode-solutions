class Solution:
    def trap(self, height: list[int]) -> int:
        left_max_array = [0] * len(height)
        right_max_array = [0] * len(height)
        rain_water = 0

        left_max = 0
        right_max = 0

        for i, h in enumerate(height):
            left_max_array[i] = left_max
            left_max = max(left_max, h)
            right_max_array[-i - 1] = right_max
            right_max = max(right_max, height[-i - 1])

        for i, h in enumerate(height):
            water_level = min(left_max_array[i], right_max_array[i]) - h
            if water_level > 0:
                rain_water += water_level

        return rain_water

solution = Solution()
print('Should return 6:', solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print('Should return 9:', solution.trap([4,2,0,3,2,5]))
