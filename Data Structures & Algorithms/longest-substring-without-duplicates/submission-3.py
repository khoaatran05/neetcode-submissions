class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()

        left = 0
        right = 0

        longest = 0

        while right < len(s):

            while(s[right] in seen):
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])

            right += 1

            longest = max(longest, len(seen))
        
        return longest


            


        