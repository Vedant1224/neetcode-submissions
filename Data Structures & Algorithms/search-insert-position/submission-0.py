class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        point = 0
        for num in nums:
            if num == target:
                return nums.index(num)
            elif num> target:
                return point
            else:
                point+= 1
        return len(nums)

        
        
        