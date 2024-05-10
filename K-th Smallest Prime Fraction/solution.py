class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        l, r = 0, 1

        while l <= r:
            mid = l + (r-l)/2
            j, total, num, den = 1, 0, 0, 0
            maxFraction = 0

            for i in range(n):
                while j < n  and arr[i] >= arr[j] * mid:
                    j += 1
                total += n - j

                if j < n and maxFraction < arr[i] * 1.0 / arr[j]:
                    maxFraction = arr[i] * 1.0 / arr[j]
                    num, den = i, j
            
            if total == k:
                return [arr[num], arr[den]]
            
            if total > k: r = mid
            else: l = mid