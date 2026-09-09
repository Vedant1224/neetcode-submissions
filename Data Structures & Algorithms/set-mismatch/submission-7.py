class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        output = [0,0]
        my_dict = Counter(nums)
        for i in range(1, len(nums)+1):
            if my_dict[i] == 0:
                output[1] = i
            if my_dict[i] == 2:
                output[0] = i

        return output


        