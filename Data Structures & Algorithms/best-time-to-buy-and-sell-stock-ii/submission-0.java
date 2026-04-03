class Solution {

    public int maxProfit(int[] prices) {
        int total_profit = 0, buy = prices[0], profit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] - buy < profit) {
                total_profit += profit;
                buy = prices[i];
                profit=0;
            } else {
                profit = Math.max(profit, prices[i] - buy);
            }
        }
        return Math.max(profit, total_profit + profit);
    }
}