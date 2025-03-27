from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            look = target - value
            if look in hashmap:
                return [hashmap[look], index]
            hashmap[value] = index
                
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15, 26]
    target = 9
    expected = [0, 1] 
    output = solution.twoSum(nums, target)
    print(f"Input: {nums}, Target: {target} -> Expected: {expected} | Got: {output}")