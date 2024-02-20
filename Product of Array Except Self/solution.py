class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1  -1  -1  0  0
        # 0   0   9  0  0
        res = [0] * len(nums)
        temp = 1
        for i in range(len(nums)):
            res[i] = temp
            temp *= nums[i]
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= temp
            temp *= nums[i]
        return res