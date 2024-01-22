/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let left = right = total = 0
    let res = Number.MAX_VALUE
    while (left <= right && right != nums.length){
        total += nums[right]
        while(total >= target && left <= right){
            res = Math.min(res, right - left + 1)
            total -= nums[left]
            left++
        }
        right++
    }
    if (total >= target) res = Math.min(res, right - left + 1)
    return res == Number.MAX_VALUE? 0 : res
};