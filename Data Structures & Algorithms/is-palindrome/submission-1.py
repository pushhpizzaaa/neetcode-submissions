class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        rev = ""

        for char in cleaned:
            rev = char + rev

        return cleaned == rev