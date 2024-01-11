class Solution {
public:
    string getPermutation(int n, int k) {
        string permutation = "";

        vector<int> unused;
        for (int i = 1; i<= n; i++) unused.push_back(i);

        vector<int> fact;
        fact.push_back(1);
        for (int i = 1; i <= n; i++){
            fact.push_back(i * fact[i-1]);
        }

        k--;
        while (n > 0){
            int col = fact[n] / n;
            int i = k / col;
            permutation += to_string(unused[i]);
            auto it = find(unused.begin(), unused.end(), unused[i]);
            unused.erase(it);
            n--;
            k %= col;
        }
        return permutation;
    }
};