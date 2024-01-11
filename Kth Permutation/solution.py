class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutation = ""
        unused = [i for i in range(1, n+1)]
        fact = [1] * (n+1)
        for i in range(1, n+1):
            fact[i] = i * fact[i-1]
        k-=1
        while (n > 0):
            col = fact[n] // n
            i = k // col
            permutation += str(unused[i])
            unused.pop(i)
            n-=1
            k %= col
        return permutation