class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i = 0
        j = 0
        merged = ""

        while i < min(len(word1), len(word2)) and j < min(len(word1), len(word2)):

            merged += word1[i]
            merged += word2[j]

            i+=1
            j+=1
        

        if len(word1) > len(word2):
            while i < len(word1):
                merged += word1[i]
                i+=1
        
        if len(word2) > len(word1):
            while j < len(word2):
                merged += word2[j]
                j+=1

        return merged

        