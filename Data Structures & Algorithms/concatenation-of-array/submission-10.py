class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums.copy()
        ans = []
        for i in range(2):
            for element in nums:
                ans.append(element)
        return ans
            

        