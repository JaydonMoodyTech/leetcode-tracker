from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        list_sums = []
        for i in accounts:
             list_sums.append(sum(i))
        return max(list_sums)

if __name__ == "__main__":
    solution = Solution()
    accounts = [[2,8,7],[7,1,3],[1,9,5]]
    expected = 17
    output = solution.maximumWealth(accounts)
    print(f"Input {accounts} -> Expected: {expected} | Got: {output}")