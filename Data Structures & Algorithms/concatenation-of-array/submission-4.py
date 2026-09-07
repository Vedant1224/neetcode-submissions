class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for element in nums:
                ans.append(element)
        return ans
            

        