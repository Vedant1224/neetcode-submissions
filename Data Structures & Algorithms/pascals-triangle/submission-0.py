class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [1]
        output = []

        for _ in range(numRows):
            next_row = [1]

            for i in range(len(row)-1):
                next_row.append(row[i]+row[i+1])

            next_row.append(1)

            output.append(row)
            row = next_row

        return output
        
        
        