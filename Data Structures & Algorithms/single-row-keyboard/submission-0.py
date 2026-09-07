class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pointer = 0
        prevpointer = 0
        time = 0
        for char in word:
            prevpointer = pointer
            pointer = keyboard.index(char)
            time+= abs(pointer-prevpointer)
        return time



        