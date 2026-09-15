class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomMap = Counter(ransomNote)
        magazineMap = Counter(magazine)

        if ransomMap & magazineMap == ransomMap:
            return True
        
        return False
