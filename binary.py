def binarySearch(arr, k, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [5,2,4,1,8,9,7]
arr.sort()
k = 7
result = binarySearch(arr, k, 0, len(arr)-1)
if result != -1:
    print("Element is present")
else:
    print("Not found")