class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        count = 0
        sum=0
        weight.sort()
        for i in range(len(weight)):
            if 5000>= weight[i] + sum:
                count+=1
                sum+=weight[i]
        return count
        