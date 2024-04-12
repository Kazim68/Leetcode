/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let combs = [];
    generate(2*n, 0, "", combs);
    return combs;
};

generate = (n, diff, comb, combs) => {
    
    if (diff < 0 || diff > n) return;

    else if (n === 0 && diff === 0) combs.push(comb);

    else{
        comb += "(";
        generate(n-1, diff+1, comb, combs);
        comb = comb.slice(0, -1);
        comb += ")";
        generate(n-1, diff-1, comb, combs);
        comb = comb.slice(0, -1);
    }
}