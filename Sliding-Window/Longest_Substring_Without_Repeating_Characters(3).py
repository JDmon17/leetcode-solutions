class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenChars = set()
        maxLength = 0
        left = 0

        if (len(s) == 0):
            return 0

        for right in range(len(s)):
            while (s[right] in seenChars):
                seenChars.remove(s[left])
                left += 1

            seenChars.add(s[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength
