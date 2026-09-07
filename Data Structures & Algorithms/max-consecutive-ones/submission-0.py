class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxs = 0
        nums.append(0)
        for i in range(len(nums)):
            if nums[i] == 1:
                counter+= 1
            elif nums[i] == 0:
                if maxs < counter:
                    maxs = counter
                counter = 0
        return maxs

        