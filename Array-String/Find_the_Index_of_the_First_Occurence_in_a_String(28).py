class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenhay = len(haystack)
        lenneedle = len(needle)

        for i in range(lenhay - lenneedle + 1):
            if (haystack[i:i+lenneedle] == needle):
                return i
        
        return -1