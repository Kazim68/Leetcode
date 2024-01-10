/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    let rem = 0
    let prev = 0
    let candidate = 0
    for (let i = 0; i < gas.length; i++){
        rem += gas[i] - cost[i]
        if (rem < 0){
            prev += rem
            rem = 0
            candidate = i + 1
        }
    }
    return rem + prev < 0? -1:candidate
};