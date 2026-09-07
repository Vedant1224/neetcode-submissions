class Solution:
    def scoreOfString(self, s: str) -> int:
        newstring = s[::-1]
        total = 0
        for i in range(len(newstring)-1):
            total += abs(ord(newstring[i]) - ord(newstring[i+1]))
        return total

        