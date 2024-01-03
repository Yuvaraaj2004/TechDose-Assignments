class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(arr, l, r, e):
            if l > r:
                return -1
            pivot, i, j = r, l, r
            while i < j:
                while i < len(arr) and arr[pivot] > arr[i]:
                    i += 1
                while j >= 0 and arr[pivot] <= arr[j]:
                    j -= 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]

            arr[pivot], arr[i] = arr[i], arr[pivot]

            if i == e:
                return arr[e]
            elif i < e:
                return quickSelect(arr, i+1, r, e)
            else:
                return quickSelect(arr, l, i-1, e)

        return quickSelect(nums, 0, len(nums)-1, len(nums)-k)
