class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left = 0
        right = 0
        n = len(nums)-1
        temp = 0
        res = []
        for i in range(n+1):
            if i > 0 and a == nums[i] * -1: continue
            a = -1 * nums[i]
            right = n
            left = i+1
            while left < right:
                temp = nums[left] + nums[right]
                if temp == a: 
                    res.append([-1*a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                elif temp > a: right-=1
                elif temp < a: left+=1
        return res
            