class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        left = 0
        right = len(s1)

        freq = {}

        for i in range(len(s1)):
            if s2[i] not in freq:
                freq[s2[i]] = 1
            else:
                freq[s2[i]] += 1

        counts = {}

        for char in s1:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1

        while right < len(s2):

            if freq == counts:
                return True

            if s2[right] not in freq:
                freq[s2[right]] = 1
            else:
                freq[s2[right]] += 1


            freq[s2[left]] -= 1

            if freq[s2[left]] == 0:
                del freq[s2[left]]

            left += 1
            right += 1

        return freq == counts