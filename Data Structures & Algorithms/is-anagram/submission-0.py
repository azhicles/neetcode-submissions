class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        letters = {}
        for i in s: 
            if i in letters: 
                letters[i] += 1
            else: 
                letters[i] = 1
        
        for j in t: 
            if j in letters: 
                letters[j] -= 1
            else: 
                return False
        
        for k, v in letters.items(): 
            if v != 0: 
                return False 
        
        return True