
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - buy
            if prices[i] < buy:
                buy = prices[i]
            if profit > maxProfit:
                maxProfit = profit
        
        return maxProfit

# Runner code with sample input
if __name__ == "__main__":
    # Sample test cases
    test_cases = [
        [7,1,5,3,6,4],        # Expected output: 5
        [7,6,4,3,1],          # Expected output: 0
        [2,4,1],              # Expected output: 2
        [1],                  # Expected output: 0
    ]
    
    solution = Solution()
    
    # Test each case
    for prices in test_cases:
        profit = solution.maxProfit(prices)
        print(f"Prices: {prices}")
        print(f"Maximum profit: {profit}")
        print("-" * 50)
                