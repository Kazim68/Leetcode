class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [0 for i in range(len(matrix[0]) + 1)]
        prev = [0 for i in range(len(matrix[0]) + 1)]
        res = 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] == "1":
                    dp[j] = min(prev[j], prev[j-1], dp[j-1]) + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
            prev = dp[:]
        return res * res