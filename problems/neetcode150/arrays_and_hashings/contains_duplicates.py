from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for x in range(len(nums)- 1):
            if nums[x] == nums[x+1]:
                return True
        return False
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 1]
    expected = True
    output = solution.hasDuplicate(nums)
    print(f"Input: {nums} -> Expected: {expected} | Got: {output}")