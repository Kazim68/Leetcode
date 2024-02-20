/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let left = 0
    let right = numbers.length-1
    let temp = 0
    while (left < right){
        temp = numbers[left]+numbers[right]
        if (temp == target) break
        else if (temp > target) right--
        else left++
    }
    return [left+1, right+1]
};