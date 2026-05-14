class Solution:
    def isPalindrome(self, s: str) -> bool:
        comp = ''
        for char in s:
            if char.isalnum():
                comp += char.lower()
        return comp == comp[::-1]
