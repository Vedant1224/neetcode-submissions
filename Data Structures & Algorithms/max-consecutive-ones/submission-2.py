class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxs = 0
        for num in nums:
            if num ==1:
                counter += 1
            else:
                maxs = max(maxs, counter)
                counter = 0
        return max(maxs, counter)

        