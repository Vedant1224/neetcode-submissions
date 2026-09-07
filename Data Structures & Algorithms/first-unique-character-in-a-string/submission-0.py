class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict = Counter(s)
        for key, value in mydict.items():
            if value == 1:
                return s.index(key)
            else:
                continue

        return -1


        