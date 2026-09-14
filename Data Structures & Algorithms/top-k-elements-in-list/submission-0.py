class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        count=0
        my_dict = Counter(nums)
        sorted_dict = sorted(my_dict.items(), key = lambda item: item[1], reverse = True)
        while k > 0:
            output.append(sorted_dict[count][0])
            count+=1
            k-=1
        return output
            
        