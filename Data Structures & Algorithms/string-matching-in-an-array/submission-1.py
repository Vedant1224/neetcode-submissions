class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output=[]
        for word in words:
            for other_word in words:
                if word != other_word and word in other_word:
                    output.append(word)
                    break
        return output

        