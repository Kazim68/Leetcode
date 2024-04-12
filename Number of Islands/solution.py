class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        count = 0
        n = len(grid)
        m = len(grid[0])
        for row in range(n):
            for col in range(m):
                if self.explore(grid, visited, row, col, n, m):
                    count+=1
        return count
    
    def explore(self, grid, visited,row, col, n, m):
        rowCheck = row >= 0 and row < n
        colCheck = col >= 0 and col < m
        if not rowCheck or not colCheck: return False
        if grid[row][col] == "0": return False
        key = str(row) + ',' + str(col)
        if key in visited: return False
        visited[key] = 1
        self.explore(grid, visited, row+1, col, n, m)
        self.explore(grid, visited, row-1, col, n, m)
        self.explore(grid, visited, row, col+1, n, m)
        self.explore(grid, visited, row, col-1, n, m)
        return True
        