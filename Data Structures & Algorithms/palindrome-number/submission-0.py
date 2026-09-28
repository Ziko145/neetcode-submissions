class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = [i for i in str(x)]
        return (s == s[::-1])
        