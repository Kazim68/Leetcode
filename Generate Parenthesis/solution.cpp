class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string>* combinations = new vector<string>();
        generate(2*n, 0, "", combinations);
        return *combinations;
    }

    void generate(int n, int diff, string comb, vector<string>* combinations){

        if (diff < 0 || diff > n) return;

        else if (n == 0 && diff == 0) {
            combinations->push_back(comb);
        }

        else {
            comb.push_back('(');
            generate(n-1, diff+1, comb, combinations);
            comb.pop_back();
            comb.push_back(')');
            generate(n-1, diff-1, comb, combinations);
            comb.pop_back();
        }
    }
};