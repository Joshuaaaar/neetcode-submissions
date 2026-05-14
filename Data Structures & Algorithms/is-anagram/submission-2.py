class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if not the same length return false 
        if len(s) != len(t):
            return False 
        
        # hashmap of s
        hash_map_s = {} 

        for char in s:
           # print(hash_map_s)
            if char in hash_map_s:
                hash_map_s[str(char)] += 1 
            else:
                hash_map_s[str(char)] = 1
        
        # hashmap of t
        hash_map_t = {}

        for char1 in t:
            if char1 not in hash_map_t:
                hash_map_t[char1] = 1
            else:
                hash_map_t[char1] += 1
        
        for checking in s:

            if checking not in hash_map_t:
                return False 
            
            occur = hash_map_t[checking]

            if occur != hash_map_s[checking]:
                return False 
        
        return True

        
        
        