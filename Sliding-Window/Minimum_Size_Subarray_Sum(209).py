class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        minLength = float('inf')
        total = 0

        for right in range(len(nums)):
            total += nums[right]

            while (total >= target):
                minLength = min(right - left + 1, minLength)
                total -= nums[left]
                left += 1
        
        return minLength if minLength != float('inf') else 0