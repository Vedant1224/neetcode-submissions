class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict = Counter(nums)
        return max(mydict, key =mydict.get)

        