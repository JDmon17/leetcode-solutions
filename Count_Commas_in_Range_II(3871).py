class Solution:
    def countCommas(self, n: int) -> int:
        p = 1000
        result = 0
        while p <= n:
            result += n - p + 1
            p *= 1000
        return result