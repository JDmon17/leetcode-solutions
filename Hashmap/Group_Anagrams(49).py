class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramMap = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            anagramMap[sortedWord].append(word)
        
        return list(anagramMap.values())