class Solution {
public:
    int minimumCost(vector<int>& cost) {
        sort(cost.begin(), cost.end());
        int amount = 0;
        int c = 0;
        for (int i = cost.size() -1; i >= 0; i--){
            c++;
            if (c == 3) c = 0;
            else{
                amount += cost[i];
            }
        }
        return amount;
    }
};