class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        my_dict = Counter(arr)
        distinct = []
        for key, value in my_dict.items():
            if value == 1:
                distinct.append(key)
        if  len(distinct) == 0 or k > len(distinct):
            return ""
        else:
            return distinct[k-1]
        