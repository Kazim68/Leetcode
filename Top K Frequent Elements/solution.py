class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bank = {}
        for num in nums:
            if num in bank:
                bank[num] += 1
            else:
                bank[num] = 1
        bucket = [0] * (len(nums) + 1)
        for key in bank:
            if not bucket[bank[key]]:
                bucket[bank[key]] = []
            bucket[bank[key]].append(key)
        res = []
        idx = 0
        for values in reversed(bucket):
            if values:
                for value in values:
                    res.append(value)
                    idx += 1
                    if idx == k: return res
        return res
        