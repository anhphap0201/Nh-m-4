import random

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

def bogosort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

# Example usage
arr = [4, 2, 7, 1, 5]
sorted_arr = bogosort(arr)
print(sorted_arr)
