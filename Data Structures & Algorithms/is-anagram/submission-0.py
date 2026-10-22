class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 ={}

        for char in s:
            hash1[char] = hash1.get(char, 0) + 1
        
        for char in t:
            hash2[char] = hash2.get(char, 0) + 1

                # Python dictionaries can be compared directly for equality
        if len(s) != len(t):
            return False
        return hash1 == hash2
       

        
