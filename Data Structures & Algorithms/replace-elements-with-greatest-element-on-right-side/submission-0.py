class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for idx, num in enumerate(arr):
            if idx+1 < len(arr):
                arr[idx] = max(arr[idx+1:])
            else:
                arr[idx] = -1
        return arr        