def validMountainArray(self, arr):
    i = 1
    while i < len(arr) and arr[i] > arr[i - 1]:
        i += 1
    if i == len(arr) or i == 1:
        return False
    while i < len(arr) and arr[i] < arr[i - 1]:
        i += 1
    return i == len(arr)
