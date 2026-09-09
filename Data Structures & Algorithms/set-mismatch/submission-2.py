class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        output = []
        my_dict = Counter(nums)
        for key, value in my_dict.items():
            if value == 2:
                output.append(key)



        for i in range(1,len(nums)+1):
            if i not in nums:
                output.append(i)

        return output


        