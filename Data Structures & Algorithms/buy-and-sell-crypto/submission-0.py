class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        left = 0
        right = 1
        N = len(prices)

        while (right < N):
            profit = prices[right] - prices[left]

            maxProfit = max(maxProfit, profit)

            if (left == right):
                right += 1
            
            elif (prices[left] < prices[right]):
                right += 1
            else:
                left += 1
        
        return maxProfit

