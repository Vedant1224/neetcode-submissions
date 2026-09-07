class Solution:
    def confusingNumber(self, n: int) -> bool:
        mystr = str(n)
        mapping = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        rotatedValue = []

        for num in mystr[::-1]:
            if num not in mapping:
                return False
            rotatedValue.append(mapping[num])
        rotated = "".join(rotatedValue)
        if rotated != mystr:
            return True
        return False