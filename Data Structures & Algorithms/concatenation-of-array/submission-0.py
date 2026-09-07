class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = nums.copy()
        starting_index = len(new_list)
        for element in nums:
            new_list.append(element)
        return new_list     