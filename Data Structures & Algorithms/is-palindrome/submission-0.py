class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        rev = ""

        for i in s:
            rev = i + rev
        
        if s == rev:
            return True
        return False