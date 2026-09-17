class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        if len(pattern) != len (words):
            return False
        
        seen = {}

        for p, w in zip(pattern, words):
            keyP = ("p", p)
            keyW = ("w", w)

            if (keyP in seen and seen[keyP] != w):
                return False
            if (keyW in seen and seen[keyW] != p):
                return False
            
            seen[keyP] = w
            seen[keyW] = p
        
        return True