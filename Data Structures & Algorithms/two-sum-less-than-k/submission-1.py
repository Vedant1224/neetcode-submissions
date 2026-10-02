class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        total = 0
        maxsum = 0
        nums.sort(reverse = True)
        for i in range(len(nums)):
            if nums[i] < k:
                total += nums[i]
                for j in range(i, len(nums)):
                    if i !=j and nums[j] + total < k:
                        total+= nums[j]
                        maxsum = max(total, maxsum)
                        total = 0
            else:
                continue

        return maxsum or -1


        