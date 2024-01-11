/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    let adj = {};

    for (let i = 0; i < prerequisites.length; i++) {
        const source = prerequisites[i][0];
        const destination = prerequisites[i][1];

        if (!adj[destination]) adj[destination] = [];
        adj[destination].push(source);
    }

    const visited = {};

    for (let i = 0; i < numCourses; i++) {
        if (!visited[i]) {
            if (cycle(i, {}, visited, adj)) return false;
        }
    }

    return true;
};

const cycle = (i, path, visited, adj) => {
    visited[i] = true;
    path[i] = true;

    if (adj[i]) {
        for (let j = 0; j < adj[i].length; j++) {
            if (!visited[adj[i][j]]) {
                if (cycle(adj[i][j], path, visited, adj)) return true;
            } else if (path[adj[i][j]]) {
                return true;
            }
        }
    }

    path[i] = false;
    return false;
};

