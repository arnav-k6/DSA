def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1
# iterates through all values in the array; returns the index of the array with the target value, else returns -1


def binary_search(arr,target):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid]< target:
            low = mid+1
        elif arr[mid]>target:
            high = mid-1
    
    return -1
  # halves the searching array size each time, saving time and memory; returns the index of the array with the target value, else returns -1

