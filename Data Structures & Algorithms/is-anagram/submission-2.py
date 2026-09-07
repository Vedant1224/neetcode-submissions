class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word_s = [i for i in s]
        word_t = [i for i in t]
        word_s.sort()
        word_t.sort()
        if word_s == word_t:
            return True
        else:
            return False

        