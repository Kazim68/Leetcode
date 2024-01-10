class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        prev = 0
        candidate = 0
        rem = 0
        for i in range(len(gas)):
            rem += gas[i] - cost[i]
            if rem < 0:
                prev += rem
                candidate = i + 1
                rem = 0
        return -1 if rem + prev < 0 else candidate