class Solution {
public:
    vector<long long> minOperations(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(), nums.end());
        vector<long long> prefix(nums.size() + 1, 0);
        for (int i = 0; i < nums.size(); i++){
            prefix[i+1] = prefix[i] + nums[i];
        }
        nums.insert(nums.begin(), 0);
        vector<long long> res;
        for (auto q : queries){
            auto lower = lower_bound(nums.begin(), nums.end(), q) - nums.begin() - 1;
            auto upper = upper_bound(nums.begin(), nums.end(), q) - nums.begin();
            auto temp = q*lower - (prefix[lower] - prefix[0]);
            temp += upper != nums.size() ? prefix[nums.size()-1] - prefix[upper-1] - q*(nums.size()-upper) : 0;
            res.push_back(temp);
        }
        return res;
    }
};