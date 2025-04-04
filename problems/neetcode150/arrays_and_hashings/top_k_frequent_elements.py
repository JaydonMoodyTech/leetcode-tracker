from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        hashmap = {}
        count = 0
        for x in nums:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1
        new_list = (sorted(hashmap, key = lambda x: hashmap[x]))
        for x in range(len(new_list)-k):
            del new_list[0]
        return new_list

 if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,2,2,3] 
    k = 2
    expected = [1,2]
    outcome = solution.topKFrequent(nums, k)  
    print(f"Input: {digits} -> Expected: {expected} | Got: {output}")