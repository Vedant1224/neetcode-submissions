class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        val = 2
        while val > 0:
            for num in nums:
                ans.append(num)
            val-=1
        return ans
        

        