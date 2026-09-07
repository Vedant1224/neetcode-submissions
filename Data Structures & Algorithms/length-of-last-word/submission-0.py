class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        print(s)
        new_list = list(s)
        total = 0
        new_list.reverse()
        for i in range(len(new_list)):
            if new_list[i] == ' ':
                break
            else:
                total += 1
        return total

        