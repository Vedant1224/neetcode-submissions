class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mydict = Counter(nums)
        return min(mydict, key =mydict.get)
        