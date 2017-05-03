"""
QuickSort
- Given unsorted list of unique integers
  return a sorted array in-place using no extra memory O(n log n) runtime
"""

import random
def quicksort(arr, start, end):
    if start < end:
        center = partition(arr, start, end)
        quicksort(arr, start, center-1)
        quicksort(arr, center+1, end)
    return arr

def partition(arr, start, end):
    pivot = arr[start]
    left = start+1
    right = end

    while True:
        # move to element that needs to be on right
        while left <= right and pivot >= arr[left]:
            left += 1

        # move element to element that needs to be left
        while right >= left and pivot <= arr[right]:
            right -= 1

        if left > right:
            break

        # swap elements over wall
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    # swap pivot into place
    temp = arr[start]
    arr[start] = arr[right]
    arr[right] = temp

    # return pivot location
    return right

t = list()
for i in range(0, 1000):
    t.append(i)

random.shuffle(t)

print(quicksort(t, 0, len(t)-1))

for i in range(0, 100):
    if t[i] != i:
        print("error at " + str(i))
