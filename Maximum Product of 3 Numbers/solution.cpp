class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        if (nums.size()<3) return 0; 
        sort(nums.begin(), nums.end());
        int s = nums.size();
        return max(nums[0] * nums[1] * nums[s-1], nums[s-1]*nums[s-2]*nums[s-3]);
    }
};