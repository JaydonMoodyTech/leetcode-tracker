class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_pal = ""
        for char in s:
            if char.isalnum():
                check_pal += char.lower()
        if check_pal == check_pal[::-1]:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    expected = True
    output = solution.isPalindrome(s)
    print(f"Input {s} -> Expected: {expected} | Got: {output}")