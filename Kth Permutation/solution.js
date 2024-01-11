/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function(n, k) {
    let permutation = ""
    unused = Array(n+1).fill().map((_, i) => i + 1)
    let fact = Array(n+1);
    fact[0] = 1;
    for (let i = 1; i <= n; i++) {
        fact[i] = i * fact[i - 1];
    }
    k--;
    while (n > 0){
        let col = Math.floor(fact[n] / n)
        let i = Math.floor(k / col)
        permutation += unused[i]
        unused.splice(i, 1)
        n--
        k %= col
    }
    return permutation
};