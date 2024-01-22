class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = total = 0
        res = float('inf')
        n = len(nums)
        while (left <= right and right != n):
            total += nums[right]
            while (total >= target and left <= right):
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        res = min(res, right - left + 1) if total >= target else res
        return 0 if res == float('inf') else res