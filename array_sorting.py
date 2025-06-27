def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        j = i-1

        while j>=0 and arr[j] > value:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = value

