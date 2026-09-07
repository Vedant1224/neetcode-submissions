class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        vals = list(nums)
        for i in range(len(vals)):
            if vals[i] == 0:
                nums.remove(vals[i])
                nums.append(0)
            

