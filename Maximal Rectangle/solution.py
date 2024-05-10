class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # initialize a left and right array for keeping track 
        # of nearest smaller from each index. A monotonic stack for 
        # getting these indexes
        n = len(heights)
        left, right = [0 for i in range(n)], [0 for i in range(n)]
        stack = []
        res, temp = 0, 0
        stack.append(-1)        # -1 is acting as a stopper for left side

        # loop through all the heights and fill left array using stack
        for i in range(n):
            temp = stack[-1]
            while temp != -1 and heights[i] <= heights[temp]:
                stack.pop()
                temp = stack[-1]
            left[i] = temp
            stack.append(i)
        
        # now for right heights
        stack = []
        stack.append(n)        # right stopper
        for i in range(n-1, -1, -1):
            temp = stack[-1]
            while temp != n and heights[i] <= heights[temp]:
                stack.pop()
                temp = stack[-1]
            right[i] = temp
            stack.append(i)
            # also checking for the max area
            res = max(res, heights[i] * (right[i] - left[i] - 1))
        return res

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        heights = [int(num) for num in matrix[0]]
        res = 0

        for i in range(n):
            for j in range(m):
                if i == 0: continue
                if matrix[i][j] == "0": heights[j] = 0
                else: heights[j] += int(matrix[i][j])
            res = max(res, self.largestRectangleArea(heights))
        return res