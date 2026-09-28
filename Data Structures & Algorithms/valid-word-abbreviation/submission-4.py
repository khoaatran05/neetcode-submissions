class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = 0
        j = 0
        num = 0
        
        while j < len(abbr):

            if abbr[j] == '0':
                return False
            
            num = 0

            if abbr[j].isdigit():
                num = int(abbr[j])

                while j + 1 < len(abbr) and abbr[j + 1].isdigit():
                    j += 1
                    num *= 10
                    num += int(abbr[j])

                i += num
                j += 1

                if i > len(word):
                    return False

                if j == len(abbr):
                    break

            if i >= len(word) or word[i] != abbr[j]:
                return False
            
            j += 1
            i += 1
        
        return i == len(word)