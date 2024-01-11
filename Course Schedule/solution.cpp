class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        bool *visited = new bool[numCourses+1];
        for (int i = 0; i <= numCourses; i++) {
            visited[i] = false;
        }

        vector<vector<int>> adj(numCourses + 1);
        for (int i = 0; i <prerequisites.size(); i++){
            adj[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }

        for (int i = 0; i <= numCourses; i++){
            if (!visited[i] && adj[i].size()){
                vector<bool> path(numCourses+1, false);
                if (detectCycle(i, path, visited, adj)) return false;
            }
        }
        return true;
    }

    bool detectCycle(int i, vector<bool>& path, bool visited[], vector<vector<int>>& adj){
        visited[i] = true;
        path[i] = true;
        for (int j = 0; j < adj[i].size(); j++){
            if (!visited[adj[i][j]]){
                if (detectCycle(adj[i][j], path, visited, adj)) return true;
            }
            else if (path[adj[i][j]]) return true;
        }
        path[i] = false;
        return false;
    }
};