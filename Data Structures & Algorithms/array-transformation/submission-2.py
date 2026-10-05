class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        decision = True
        new_arr = arr[:]
        while decision:
            for i in range(1,len(arr)-1):
                if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                    new_arr[i]-=1
                elif arr[i] < arr[i+1] and arr[i] < arr[i-1]:
                    new_arr[i]+=1
            if new_arr == arr:
                decision = False
            else:
                arr = new_arr[:]
        return arr
        