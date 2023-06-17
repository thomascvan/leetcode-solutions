class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
        return max_profit

solution = Solution()
print('Should return 5:', solution.maxProfit([7,1,5,3,6,4]))
print('Should return 0:', solution.maxProfit([7,6,4,3,1]))
print('Should return 8:', solution.maxProfit([1,2,4,2,5,7,2,4,9,]))
print('Should return 9:', solution.maxProfit([1,2,4,2,5,7,2,4,9,0,9]))