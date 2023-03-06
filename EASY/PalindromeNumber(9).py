class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s=str(x)
        s=s[::-1]
        p=int(s)
        if (x==p):
            return True
        else:
            return False