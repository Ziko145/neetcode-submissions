class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filtered = ""
        for i in s:
            if i.isalnum():
                filtered += i
        return filtered == filtered[::-1]