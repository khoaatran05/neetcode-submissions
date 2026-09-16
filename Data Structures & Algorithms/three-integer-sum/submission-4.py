class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        
        ordered = sorted(nums)
        result = []

        for i in range(len(ordered)):
            if i > 0 and ordered[i] == ordered[i-1]:
                continue

            needed = -ordered[i]
            
            left = i+1
            right = len(ordered) - 1
            while left < right:
                if ordered[left] + ordered[right] == needed:
                    result.append([ordered[left],ordered[right],ordered[i]])
                    left+=1
                    right -=1

                    while left < right and ordered[left] == ordered[left -1]:
                        left += 1
                    while left < right and ordered[right] == ordered[right +1]:
                        right -=1

                elif ordered[left] + ordered[right] < needed:
                    left += 1
                else:
                    right -=1
                

            
        return result




            


        