class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0, right = 0, total = 0, res = INT_MAX, n = nums.size();
        while (left <= right && right != n){
            total += nums[right];
            while (total >= target && left <= right){
                res = min(res, right - left + 1);
                total -= nums[left];
                left++;
            }
            right++;
        }
        if (total >= target) res = min(res, right - left + 1);
        return res == INT_MAX ? 0 : res;
    }
};