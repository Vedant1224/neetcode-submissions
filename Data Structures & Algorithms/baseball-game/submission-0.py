class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []

        for i in range(len(operations)):
            if operations[i] == "+":
                sumval = output[-1] + output[-2]
                output.append(sumval)
            
            elif operations[i] == "D":
                multval = output[-1] *2
                output.append(multval)
            
            elif operations[i] == "C":
                output.pop()

            else :
                output.append(int(operations[i]))

        return sum(output)

            

        