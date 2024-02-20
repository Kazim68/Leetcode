class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet:
                size = 1
                while (num + size) in numSet:
                    size += 1
                longest = max(longest, size)
        return longest