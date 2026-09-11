class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        currMax = 0
        for num in nums:
            if num == 1:
                counter+=1
            else:
                currMax = max(counter,currMax)
                counter = 0
        return max(counter, currMax)
