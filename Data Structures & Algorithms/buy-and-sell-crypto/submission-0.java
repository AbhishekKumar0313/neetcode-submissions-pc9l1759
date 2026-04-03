class Solution {

    public int maxProfit(int[] prices) {
        int n = prices.length;
        int buy = prices[0], profit = 0;
        for (int i = 1; i < n; i++) {
            profit = Math.max(profit, prices[i] - buy);
            buy = Math.min(prices[i], buy);
        }
        return profit;
    }
}
