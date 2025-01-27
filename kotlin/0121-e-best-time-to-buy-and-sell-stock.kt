// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution {
    fun maxProfit(prices: IntArray): Int {
        var buy = prices[0]
        var maxProfit = 0

        for (i in 1 until prices.size) {
            if (prices[i] < buy) {
                buy = prices[i]
            } else {
                val profit = prices[i] - buy
                if (profit > maxProfit) {
                    maxProfit = profit
                }
            }
        }

        return maxProfit
    }
}