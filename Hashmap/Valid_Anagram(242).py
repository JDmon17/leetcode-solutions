class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashS = Counter(list(s))
        hashT = Counter(list(t))

        if hashS == hashT:
            return True
        
        return False