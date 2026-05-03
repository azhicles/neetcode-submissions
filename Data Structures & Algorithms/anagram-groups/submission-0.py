class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list) 
        for string in strs: 
            freq = [0] * 26
            for char in string: 
                idx = ord(char) - ord('a')
                freq[idx] += 1
            
            anagrams[tuple(freq)].append(string)
        
        return list(anagrams.values())

