class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxp = 0
        for right in range(len(prices)):
            if prices[right]-prices[left]<0:
                right+=1
                left+=1
            else:
                profit = prices[right]-prices[left]
                maxp = max(maxp,profit)
                right+=1
        return maxp