class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total = 0
        maxsum = 0
        nums.append(0)
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                total+= nums[i]
            else:
                total+= nums[i]
                maxsum = max(total, maxsum)
                total = 0
        return maxsum

        