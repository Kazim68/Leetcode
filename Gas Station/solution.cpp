class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int candidate = 0, rem = 0, prevRem = 0;
        for (int i = 0; i < gas.size(); i++){
            rem += gas[i] - cost[i];
            if (rem < 0){
                candidate = i + 1;
                prevRem += rem;
                rem = 0;
            }
        }

        if (candidate == gas.size() || rem + prevRem < 0) return -1;
        return candidate;
    }
};