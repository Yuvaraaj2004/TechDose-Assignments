def merge(l):
    def Divide(arr, l, r):
        if l >= r:
            return
        else:
            m = l+(r-l)//2
            Divide(arr, l, m)
            Divide(arr, m+1, r)
            Merge(arr, l, m, r)

    def Merge(arr, l, m, r):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        n1, n2 = len(left), len(right)
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1
    (Divide(l, 0, len(arr)))
    print(l)


def bubble(l):
    for i in range(len(l)):
        swap = False
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                swap = True
                l[j], l[j+1] = l[j+1], l[j]
        if not swap:
            break
    print(l)


def selection(l):
    for i in range(len(l)):
        maxi = i
        for j in range(i+1, len(l)):
            if l[maxi] > l[j]:
                maxi = j
        l[i], l[maxi] = l[maxi], l[i]
    print(l)


def insertion(l):
    for i in range(len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
    print(l)


def QuicSort(arr):
    def Sort(low=0, high=len(arr)-1):
        pivot, l, r = 0, low, high
        while l < r:
            while l < len(arr) and arr[l] > arr[pivot]:
                l += 1
            while r > -1 and arr[r] <= arr[pivot]:
                r -= 1
            if l < r:
                arr[l], arr[r] = arr[r], arr[l]
                r -= 1
        arr[pivot], arr[l] = arr[l], arr[pivot]
        print(arr)
    Sort()


def radix(nums, b=12):
    mx = max(nums)
    k = 1
    while mx//k:
        l = [0 for i in range(b)]
        for i in range(len(nums)):
            l[nums[i]//k % b] += 1
        for i in range(1, b):
            l[i] += l[i-1]
        arr = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            arr[l[nums[i]//k % b]-1] = nums[i]
            l[nums[i]//k % b] -= 1
        for i in range(len(nums)):
            nums[i] = arr[i]
        k *= b
    return arr


def quickSelect(arr, l, r, e, c=0):
    if l > r or e > len(arr):
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
    # print(arr[l:r+1])
    # quickSelect(arr,i+1,r,e)
    # quickSelect(arr,l,i-1,e)
    if i == e:
        print(e, arr[e], c)
    else:
        if i < e:
            quickSelect(arr, i+1, r, e, c+1)
        else:
            quickSelect(arr, l, i-1, e, c+1)


arr = [170, 45, 75, 90, 802, 24, 2, 66]
# QuicSort(arr)
# print(radix(arr[::]))
print(quickSelect(arr, 0, len(arr)-1, 10))
for i in range(0, len(arr)):
    quickSelect(arr[::], 0, len(arr)-1, i)
print(arr)
