class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        count = 0
        stack = []

        for log in logs:

            if (len(log) == 2 and log[0] != '.') or (len(log) >= 3 and log[-2] != '.' and log[-3] != '.'):
                count += 1
            elif log == '../' and count > 0:
                count -= 1
        
        return count

