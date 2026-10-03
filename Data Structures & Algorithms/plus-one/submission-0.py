class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                if i != 0:
                    digits[i] = 0
                else:
                    digits[i] = 0
                    output = [1]
                    for num in digits:
                        output.append(num)
                    return output
        return digits