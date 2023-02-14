def counting_sort(arr):
    pass


def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    pass

lst = [0,4,1,2,1,2,4,3]
print(bubble_sort(lst))