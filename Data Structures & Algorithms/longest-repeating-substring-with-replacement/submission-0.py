class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        longest = 0

        freq = {} 
        
        for right in range(len(s)):
            
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1

            maxFreq = max(freq.values())

            while (right-left+1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
                maxFreq = max(freq.values())
            
            longest = max(longest,right - left + 1)
        return longest

