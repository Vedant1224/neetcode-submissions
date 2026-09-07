class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        mydict = {num: nums.count(num) for num in nums }  
        sorteddict = {k:v for k,v in sorted(mydict.items(),reverse = True)}
        for key, value in sorteddict.items():
            if value == 1:
                return key
                break
        return -1

 
