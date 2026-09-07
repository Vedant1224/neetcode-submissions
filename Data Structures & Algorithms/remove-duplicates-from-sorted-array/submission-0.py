class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_list = []
        for i in range(len(nums)):
            if nums[i] in my_list:
                continue
            else:
                my_list.append(nums[i])
        for i in range(len(my_list)):
            nums[i] = my_list[i]
        return len(my_list)

        