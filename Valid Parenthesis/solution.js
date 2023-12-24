/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    const open = ['(', '[', '{'];
    const close = [')', ']', '}'];

    for (const bracket of s){
        if (open.includes(bracket)){
            stack.push(bracket);
        }
        else{
            if (stack.length == 0) return false;
            if (stack.pop() != open[close.indexOf(bracket)]) return false
        }
    }
    return stack.length == 0? true:false
};