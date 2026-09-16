class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for word in strs:
            curdict = {}
            for char in word:
                if char not in curdict:
                    curdict[char] = 1
                else:
                    curdict[char] += 1
            
            key = tuple(sorted(curdict.items()))

            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        
        return list(hashmap.values())
                


        