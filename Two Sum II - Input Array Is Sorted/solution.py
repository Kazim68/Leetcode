class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        temp = 0
        while left < right:
            temp = numbers[left] + numbers[right]
            if temp == target: break
            elif temp > target: right -= 1
            else: left += 1
        return [left+1, right+1]