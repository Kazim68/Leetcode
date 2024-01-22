/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let small = prices[0]
    let profit  = 0
    for (let i = 0; i < prices.length; i++){
        profit = Math.max(profit, prices[i] - small)
        small = Math.min(small, prices[i])
    }
    return profit
};