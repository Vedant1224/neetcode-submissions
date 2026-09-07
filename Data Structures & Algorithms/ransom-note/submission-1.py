class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list1 = list(ransomNote)
        list2 = list(magazine)

        for char in list1:
            if char in list2:
                list2.remove(char)
            else:
                return False
        return True
        