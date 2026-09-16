class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        items = list(hashmap.keys())
        items.sort(key = lambda x: hashmap[x], reverse=True)
        newlist = []

        for i in range(k):
            newlist.append(items[i])
        return newlist


        