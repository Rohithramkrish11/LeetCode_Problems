class Solution:
    def maxProfit(self, prices):
        minPrice = prices[0]
        maxPrice = 0
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxPrice = max(maxPrice, prices[i] - minPrice)
        return maxPrice
prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print("Maximum profit is ",solution.maxProfit(prices))