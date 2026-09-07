class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        length = len(arr)
        arr[length-1] = -1
        return arr


        