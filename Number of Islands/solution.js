/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    
    let count = 0;
    let visited = new Set()

    for (let row  = 0; row < grid.length; row++){
        for(let col = 0; col < grid[0].length; col++){
            // explore the island
            if (explore(grid, row, col, visited)){
                count++;
            }
        }
    }

    return count;
};

const explore = (grid, row, col, visited) => {
    let rowInBound = 0 <= row && row < grid.length
    let colInBound = 0 <= col && col < grid[0].length

    if (!rowInBound || !colInBound) return false

    if (grid[row][col] === "0") return false

    let pos = row + ',' + col
    if (visited.has(pos)) return false

    visited.add(pos)

    // exploring all of the island
    explore(grid, row-1, col, visited)
    explore(grid, row+1, col, visited)
    explore(grid, row, col-1, visited)
    explore(grid, row, col+1, visited)


    return true
}