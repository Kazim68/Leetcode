class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise, hare = 0, 0
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare: break
        tracker = 0
        while True:
            tortoise = nums[tortoise]
            tracker = nums[tracker]
            if tortoise == tracker: break
        return tortoise