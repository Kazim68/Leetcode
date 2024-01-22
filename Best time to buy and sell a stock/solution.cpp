class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int small = prices[0];
        for (int i = 1; i < prices.size(); i++){
            profit = max(profit, prices[i] - small);
            small = min(small, prices[i]);
        }
        return profit;
    }
};