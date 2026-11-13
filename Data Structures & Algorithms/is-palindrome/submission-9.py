class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        for i in range (len(s)):
            k=len(s)-1-i
            if s[i] != s[k]:
                return False
        return True
        