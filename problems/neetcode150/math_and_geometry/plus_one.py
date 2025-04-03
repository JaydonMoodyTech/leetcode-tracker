from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number_string = ""
        new_list = []
        for x in digits:
            number_string += (str(x)
        plus_one = str(int(number_string) + 1)
        for char in plus_one:
            new_list.append(int(char))
        return new_list

if __name__ == "__main__":
    solution = Solution()
    digits = [4,3,2,1]
    expected = [4,3,2,2]
    output = solution.plusOne(digits)
    print(f"Input: {digits} -> Expected: {expected} | Got: {output}")