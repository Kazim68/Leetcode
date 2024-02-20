/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let res = []
    let temp = 1
    for (let i = 0; i < nums.length; i++){
        res.push(temp)
        temp *= nums[i]
    }
    temp = 1
    for (let i = nums.length-1; i >= 0; i--){
        res[i] *= temp
        temp *= nums[i]
    }
    return res;
};