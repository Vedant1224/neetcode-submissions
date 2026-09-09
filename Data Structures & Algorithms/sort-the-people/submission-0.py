class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        output = []
        my_dict = dict(zip(heights, names))
        sorted_dict = dict(sorted(my_dict.items(), reverse=True))

        for key, value in sorted_dict.items():
            output.append(value)

        return output



        