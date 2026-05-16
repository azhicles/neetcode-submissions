class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(c for c in s if c.isalnum()).lower()
        return string == string[::-1]