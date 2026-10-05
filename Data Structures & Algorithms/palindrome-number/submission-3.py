class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x > 0 and x <10:
            return True

        digits = [int(x) for x in str(x)]
        end = len(digits) -1
        start = 0

        while start <= end:
            if digits[start] != digits[end]:
                return False
            start+=1
            end -=1
        return True
        