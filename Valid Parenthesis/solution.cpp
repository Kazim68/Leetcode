class Solution {
public:

    char open[3] = {'(', '[', '{'};
    char close[3] = {')', ']', '}'};

    bool isValid(string s) {

        stack<char> brackets;
        int idx = 0;

        for (int i = 0; i < s.length(); i++){
            idx = 0;
            if (isOpen(s[i])){
                brackets.push(s[i]);
            }
            else{
                if (brackets.empty()) return false;

                idx = getOpen(s[i]);
                if (brackets.top() != open[idx]){
                    return false;
                }
                brackets.pop();
            }
        }
        if (brackets.empty())
        return true;
        return false;
    }

    bool isOpen(char c){
        for (int i = 0; i < 3; i++){
            if (open[i] == c) return true;
        }
        return false;
    }

    int getOpen(char c){
        for (int i = 0; i < 3; i++){
            if (close[i] == c) return i;
        }
        return -1;
    }
};